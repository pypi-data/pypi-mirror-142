'''
# mongodb-atlas-databaseuser

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::DatabaseUser` v1.3.0.

## Description

The databaseUsers resource lets you retrieve, create and modify the MongoDB users in your cluster. Each user has a set of roles that provide access to the project?s databases. A user?s roles apply to all the clusters in the project: if two clusters have a products database and a user has a role granting read access on the products database, the user has that access on both clusters.

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::DatabaseUser \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-DatabaseUser \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::DatabaseUser`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-databaseuser+v1.3.0).
* Issues related to `MongoDB::Atlas::DatabaseUser` should be reported to the [publisher](undefined).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk
import constructs


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :schema: apiKeyDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnDatabaseUser(
    aws_cdk.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUser",
):
    '''A CloudFormation ``MongoDB::Atlas::DatabaseUser``.

    :cloudformationResource: MongoDB::Atlas::DatabaseUser
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence["RoleDefinition"],
        username: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        labels: typing.Optional[typing.Sequence["LabelDefinition"]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence["ScopeDefinition"]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::DatabaseUser``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_name: The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param roles: Array of this user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.
        :param username: Username for authenticating to MongoDB.
        :param api_keys: 
        :param awsiam_type: If this value is set, the new database user authenticates with AWS IAM credentials.
        :param labels: Array containing key-value pairs that tag and categorize the database user.
        :param ldap_auth_type: Method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE.
        :param password: The user’s password. This field is not included in the entity returned from the server.
        :param scopes: Array of clusters and Atlas Data Lakes that this user has access to. If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.
        '''
        props = CfnDatabaseUserProps(
            database_name=database_name,
            project_id=project_id,
            roles=roles,
            username=username,
            api_keys=api_keys,
            awsiam_type=awsiam_type,
            labels=labels,
            ldap_auth_type=ldap_auth_type,
            password=password,
            scopes=scopes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserCFNIdentifier")
    def attr_user_cfn_identifier(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::DatabaseUser.UserCFNIdentifier``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserCFNIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDatabaseUserProps":
        '''Resource props.'''
        return typing.cast("CfnDatabaseUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "project_id": "projectId",
        "roles": "roles",
        "username": "username",
        "api_keys": "apiKeys",
        "awsiam_type": "awsiamType",
        "labels": "labels",
        "ldap_auth_type": "ldapAuthType",
        "password": "password",
        "scopes": "scopes",
    },
)
class CfnDatabaseUserProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        project_id: builtins.str,
        roles: typing.Sequence["RoleDefinition"],
        username: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        awsiam_type: typing.Optional["CfnDatabaseUserPropsAwsiamType"] = None,
        labels: typing.Optional[typing.Sequence["LabelDefinition"]] = None,
        ldap_auth_type: typing.Optional["CfnDatabaseUserPropsLdapAuthType"] = None,
        password: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence["ScopeDefinition"]] = None,
    ) -> None:
        '''The databaseUsers resource lets you retrieve, create and modify the MongoDB users in your cluster.

        Each user has a set of roles that provide access to the project’s databases. A user’s roles apply to all the clusters in the project: if two clusters have a products database and a user has a role granting read access on the products database, the user has that access on both clusters.

        :param database_name: The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param project_id: Unique identifier of the Atlas project to which the user belongs.
        :param roles: Array of this user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.
        :param username: Username for authenticating to MongoDB.
        :param api_keys: 
        :param awsiam_type: If this value is set, the new database user authenticates with AWS IAM credentials.
        :param labels: Array containing key-value pairs that tag and categorize the database user.
        :param ldap_auth_type: Method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE.
        :param password: The user’s password. This field is not included in the entity returned from the server.
        :param scopes: Array of clusters and Atlas Data Lakes that this user has access to. If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.

        :schema: CfnDatabaseUserProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "project_id": project_id,
            "roles": roles,
            "username": username,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys
        if awsiam_type is not None:
            self._values["awsiam_type"] = awsiam_type
        if labels is not None:
            self._values["labels"] = labels
        if ldap_auth_type is not None:
            self._values["ldap_auth_type"] = ldap_auth_type
        if password is not None:
            self._values["password"] = password
        if scopes is not None:
            self._values["scopes"] = scopes

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The user’s authentication database.

        A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.

        :schema: CfnDatabaseUserProps#DatabaseName
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Unique identifier of the Atlas project to which the user belongs.

        :schema: CfnDatabaseUserProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List["RoleDefinition"]:
        '''Array of this user’s roles and the databases / collections on which the roles apply.

        A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well.

        :schema: CfnDatabaseUserProps#Roles
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List["RoleDefinition"], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Username for authenticating to MongoDB.

        :schema: CfnDatabaseUserProps#Username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :schema: CfnDatabaseUserProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    @builtins.property
    def awsiam_type(self) -> typing.Optional["CfnDatabaseUserPropsAwsiamType"]:
        '''If this value is set, the new database user authenticates with AWS IAM credentials.

        :schema: CfnDatabaseUserProps#AWSIAMType
        '''
        result = self._values.get("awsiam_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsAwsiamType"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["LabelDefinition"]]:
        '''Array containing key-value pairs that tag and categorize the database user.

        :schema: CfnDatabaseUserProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["LabelDefinition"]], result)

    @builtins.property
    def ldap_auth_type(self) -> typing.Optional["CfnDatabaseUserPropsLdapAuthType"]:
        '''Method by which the provided username is authenticated.

        If no value is given, Atlas uses the default value of NONE.

        :schema: CfnDatabaseUserProps#LdapAuthType
        '''
        result = self._values.get("ldap_auth_type")
        return typing.cast(typing.Optional["CfnDatabaseUserPropsLdapAuthType"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The user’s password.

        This field is not included in the entity returned from the server.

        :schema: CfnDatabaseUserProps#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List["ScopeDefinition"]]:
        '''Array of clusters and Atlas Data Lakes that this user has access to.

        If omitted, Atlas grants the user access to all the clusters and Atlas Data Lakes in the project by default.

        :schema: CfnDatabaseUserProps#Scopes
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List["ScopeDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserPropsAwsiamType"
)
class CfnDatabaseUserPropsAwsiamType(enum.Enum):
    '''If this value is set, the new database user authenticates with AWS IAM credentials.

    :schema: CfnDatabaseUserPropsAwsiamType
    '''

    NONE = "NONE"
    '''NONE.'''
    USER = "USER"
    '''USER.'''
    ROLE = "ROLE"
    '''ROLE.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.CfnDatabaseUserPropsLdapAuthType"
)
class CfnDatabaseUserPropsLdapAuthType(enum.Enum):
    '''Method by which the provided username is authenticated.

    If no value is given, Atlas uses the default value of NONE.

    :schema: CfnDatabaseUserPropsLdapAuthType
    '''

    NONE = "NONE"
    '''NONE.'''
    USER = "USER"
    '''USER.'''
    GROUP = "GROUP"
    '''GROUP.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.LabelDefinition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class LabelDefinition:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: labelDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: labelDefinition#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: labelDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.RoleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "collection_name": "collectionName",
        "database_name": "databaseName",
        "role_name": "roleName",
    },
)
class RoleDefinition:
    def __init__(
        self,
        *,
        collection_name: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param collection_name: 
        :param database_name: 
        :param role_name: 

        :schema: roleDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if collection_name is not None:
            self._values["collection_name"] = collection_name
        if database_name is not None:
            self._values["database_name"] = database_name
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def collection_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#CollectionName
        '''
        result = self._values.get("collection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: roleDefinition#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ScopeDefinition",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ScopeDefinition:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["ScopeDefinitionType"] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 

        :schema: scopeDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: scopeDefinition#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ScopeDefinitionType"]:
        '''
        :schema: scopeDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ScopeDefinitionType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScopeDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-databaseuser.ScopeDefinitionType"
)
class ScopeDefinitionType(enum.Enum):
    '''
    :schema: ScopeDefinitionType
    '''

    CLUSTER = "CLUSTER"
    '''CLUSTER.'''
    DATA_LAKE = "DATA_LAKE"
    '''DATA_LAKE.'''


__all__ = [
    "ApiKeyDefinition",
    "CfnDatabaseUser",
    "CfnDatabaseUserProps",
    "CfnDatabaseUserPropsAwsiamType",
    "CfnDatabaseUserPropsLdapAuthType",
    "LabelDefinition",
    "RoleDefinition",
    "ScopeDefinition",
    "ScopeDefinitionType",
]

publication.publish()
