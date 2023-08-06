import enum
from typing import Callable, List, Optional, Set, Type
from singleton3 import Singleton

from vtb_authorizer_utils.errors import SchemaBuilderError


class ContextType(enum.Enum):
    """ Типы контекста """
    ORGANIZATIONS = 'Organizations'  # Контекст организации
    FOLDERS = 'Folders'  # Контекст папки
    PROJECTS = 'Projects'  # Контекст проекта
    DEFAULT = 'Default'  # Без контекста


class AuthorizerSchemaBuilder(metaclass=Singleton):
    """ Построение схемы импорта сервиса в Authorizer """

    def __init__(self):
        self.data = {}
        # Временное хранилище данных функций
        self._tmp_views_data = {}
        self._views = {}

    def add_service(self, name: str,
                    title: str,
                    url: str,
                    description: Optional[str] = None) -> 'AuthorizerSchemaBuilder':
        """
        Добавление информации о сервисе для импорта в Authorizer
        :param name: наименование сервиса
        :param title: понятное наименование сервиса
        :param url: url сервиса
        :param description: описание сервиса
        :return:
        """
        service_name = name.lower()
        if service_name not in self.data:
            self.data[service_name] = {
                'title': title,
                'description': description,
                'url': url,
                'resource_types': {},
                'resource_rules': []
            }

        return self

    def add_resource_type(self, service: str,
                          name: str,
                          qualified_name: Optional[str] = None,
                          title: Optional[str] = '',
                          description: Optional[str] = '',
                          cls: Optional[Type] = None) -> 'AuthorizerSchemaBuilder':
        """
        Добавление информации о ресурсном типе для импорта в Authorizer
        :param service: наименование сервиса
        :param name: наименование ресурса, именуется по аналогии с коллекцией в REST
        :param qualified_name: внутреннее наименование ресурса,
        в случае применения декоратора к классу - это view_class.__qualname__
        :param title: понятное наименование ресурса
        :param description: описание ресурса
        :return:
        """
        service = service.lower()
        if service in self.data:
            name = name.lower()
            qualified_name = cls.__qualname__ if cls else qualified_name or name 
            actions = set()
            for key, data in list(self._tmp_views_data.items()):
                view = self._views.get(key)
                if self._check_member(cls=cls, view=view, qualified_name=qualified_name, key=key):
                    value = self._tmp_views_data.pop(key)
                    action_code = _get_action_code(key)
                    resource_action_code = f'{service}:{name}:{action_code}'
                    actions.add(action_code)

                    value['resource_action_code'] = resource_action_code

                    self.data[service]['resource_rules'].append(value)

            self.data[service]['resource_types'][name] = {
                'title': title,
                'description': description,
                'actions': ','.join(actions)
            }

        return self

    def add_resource_rule(self,
                          view: Callable,
                          http_method: str,
                          url_pattern: str,
                          action_code: str,
                          access_type: str,
                          operation_name: str,
                          qualified_name: str,
                          context_types: Optional[Set[ContextType]] = None, 
                          prefixes: List[str] = None,) -> 'AuthorizerSchemaBuilder':
        """
        Добавление информации о ресурсном правиле для импорта в Authorizer
        :param http_method:
        :param url_pattern:
        :param action_code:
        :param access_type:
        :param operation_name:
        :param qualified_name:
        :param context_types:
        :return:
        """
        if prefixes:
            prefixes.append('')
        else:
            prefixes = ['']
        if context_types:
            for context_type in context_types:
                context_type = _CONTEXT_TYPES_MAP[context_type]
                for prefix in prefixes:
                    prefix_key = f"{prefix.replace('/', '_').lstrip('_')}_" if prefix else ''
                    key = f'{qualified_name}-{action_code}-{context_type}-{http_method}-{prefix}'
                    self._views[key] = view
                    self._tmp_views_data[key] = {
                        'http_method': http_method,
                        'url_pattern': f"{prefix}{url_pattern}".replace('{context_type}', context_type),
                        'access_type': access_type,
                        'operation_name': f'{prefix_key}{operation_name}',
                    }

        else:
            for prefix in prefixes:
                prefix_key = f"{prefix.replace('/', '_').strip('_')}_" if prefix else ''
                key = f'{qualified_name}-{action_code}-default-{http_method}-{prefix}'
                self._views[key] = view
                self._tmp_views_data[key] = {
                    'http_method': http_method,
                    'url_pattern': f"{prefix}{url_pattern}",
                    'access_type': access_type,
                    'operation_name': f"{prefix_key}{operation_name}",
                }

        return self

    def _check_member(
        self, 
        cls: Optional[Type] = None,
        view: Optional[Callable] = None,
        key: Optional[str] = None,
        qualified_name: Optional[str] = None
    ):
        if key is not None and qualified_name is not None:
            if str(key).startswith(qualified_name):
                return True
        if view is not None and cls is not None:
            return getattr(cls, view.__name__) is view


def authorizer_service(name: str,
                       title: str,
                       url: str,
                       description: Optional[str] = None) -> 'AuthorizerSchemaBuilder':
    """
    Добавление информации о сервисе для импорта в Authorizer, функция, которая должна быть вызвана до обработки
    декораторов, например в самом верху файла views.py
    :param name: имя сервиса
    :param title: наименование
    :param url: базовый URL сервиса, который используется для доступа через шлюз
    :param description: описание
    :return:
    """
    return AuthorizerSchemaBuilder().add_service(name,
                                                 title,
                                                 url,
                                                 description=description)


_KEY_SEPARATOR = '-'

_CONTEXT_TYPES_MAP = {
    ContextType.ORGANIZATIONS: 'organizations',
    ContextType.FOLDERS: 'folders',
    ContextType.PROJECTS: 'projects',
}
# Карта соответствия наименований функций DRF и HTTP действий
_ACTION_CODES_MAP = {
    'retrieve': 'get',
    'get': 'get',
    'list': 'list',
    'destroy': 'delete',
    'delete': 'delete',
    'create': 'create',
    'post': 'create',
    'update': 'update',
    'partial_update': 'update',
    'put': 'update',
    'patch': 'update',
}


def _get_action_code(key: str) -> str:
    """
    Формирование кода дейчтвия для правила
    :param key: ключ, например 'HealthCheckView.get-get-default-GET',
    'TagViewSet.inventory_tags-inventory_tags-projects-DELETE'
    'TagViewSet.create-create-projects-POST'
    :return:
    """
    key_parts = key.split(_KEY_SEPARATOR)
    if not key_parts or len(key_parts) < 2:
        raise SchemaBuilderError(f'Invalid key {key}')

    action_code_key = key_parts[1].lower()
    action_code_present = action_code_key in _ACTION_CODES_MAP
    action_code = _ACTION_CODES_MAP[action_code_key] if action_code_present else action_code_key.replace('_', '-')

    return action_code
