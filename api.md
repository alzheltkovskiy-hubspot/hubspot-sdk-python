# Shared Types

```python
from hubspot_sdk.types import (
    AssociationSpec,
    BatchInputString,
    Error,
    ErrorDetail,
    ForwardPaging,
    NextPage,
    Paging,
    PreviousPage,
    PublicObjectID,
    StandardError,
    VersionUser,
)
```

# Account

Types:

```python
from hubspot_sdk.types import APIUsage, CollectionResponseAPIUsage, PortalInformationResponse
```

## AuditLogs

Types:

```python
from hubspot_sdk.types.account import (
    ActingUser,
    CollectionResponseHydratedCriticalActionForwardPaging,
    CollectionResponsePublicAPIUserActionEventForwardPaging,
    CollectionResponsePublicLoginAuditForwardPaging,
    HydratedCriticalAction,
    PublicAPIUserActionEvent,
    PublicLoginAudit,
)
```

# Auth

## OAuth

Types:

```python
from hubspot_sdk.types.auth import (
    AccessTokenInfoResponse,
    RefreshTokenInfoResponse,
    TokenResponseIf,
)
```

Methods:

- <code title="post /oauth/v1/token">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">create</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/token_response_if.py">TokenResponseIf</a></code>
- <code title="delete /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">delete</a>(token) -> None</code>
- <code title="get /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get</a>(token) -> <a href="./src/hubspot_sdk/types/auth/refresh_token_info_response.py">RefreshTokenInfoResponse</a></code>

# Automation

## Actions

Types:

```python
from hubspot_sdk.types.automation import (
    BatchInputCallbackCompletionBatchRequest,
    CallbackCompletionBatchRequest,
    CallbackCompletionRequest,
    CollectionResponsePublicActionDefinitionForwardPaging,
    CollectionResponsePublicActionFunctionIdentifierNoPaging,
    CollectionResponsePublicActionRevisionForwardPaging,
    FieldTypeDefinition,
    InputFieldDefinition,
    Option,
    OutputFieldDefinition,
    PublicActionDefinition,
    PublicActionDefinitionEgg,
    PublicActionDefinitionPatch,
    PublicActionFunction,
    PublicActionFunctionIdentifier,
    PublicActionLabels,
    PublicActionRevision,
    PublicConditionalSingleFieldDependency,
    PublicExecutionTranslationRule,
    PublicObjectRequestOptions,
    PublicSingleFieldDependency,
)
```

Methods:

- <code title="post /automation/v4/actions/{appId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="patch /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">update</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">SyncPage[PublicActionRevision]</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">archive_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="post /automation/v4/actions/callbacks/{callbackId}/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete</a>(callback_id, \*\*<a href="src/hubspot_sdk/types/automation/action_complete_params.py">params</a>) -> None</code>
- <code title="post /automation/v4/actions/callbacks/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete_batch</a>(\*\*<a href="src/hubspot_sdk/types/automation/action_complete_batch_params.py">params</a>) -> None</code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">read</a>(function_id, \*, app_id, definition_id, function_type) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>

## Workflows

Types:

```python
from hubspot_sdk.types.automation import (
    APIAbTestBranchAction,
    APIActionDataValue,
    APIAppendObjectPropertyValue,
    APIAssociationDataSource,
    APIAssociationTimestampDataSource,
    APIAuthKeyWebhookAuthSettings,
    APIBlockedDate,
    APIConnection,
    APIContactFlow,
    APIContactFlowCreateRequest,
    APIContactFlowPutRequest,
    APIContactPropertyAnchor,
    APICustomCodeAction,
    APIDailyEnrollmentSchedule,
    APIDatasetFieldPropertyFilterDataSource,
    APIEnrolledArgumentPropertyFilterDataSource,
    APIEnrolledRecordPropertyFilterDataSource,
    APIEnrollmentEventPropertyValue,
    APIEnumerationOutputField,
    APIEventBasedEnrollmentCriteria,
    APIFetchedObjectPropertyValue,
    APIFlow,
    APIFlowBatchFetchFlowIDCoordinate,
    APIFlowBatchFetchMigrationFlowIDCoordinate,
    APIFlowBatchFetchMigrationWorkflowIDCoordinate,
    APIFlowBatchInput,
    APIFlowBatchMigrationInput,
    APIFlowCreateRequest,
    APIFlowEmailCampaign,
    APIFlowListing,
    APIFlowPutRequest,
    APIIncrementValue,
    APIInputVariable,
    APIListBasedEnrollmentCriteria,
    APIListBranch,
    APIListBranchAction,
    APIManualEnrollmentCriteria,
    APIMonthlyRelativeDaysEnrollmentSchedule,
    APIMonthlySpecificDaysEnrollmentSchedule,
    APIObjectPropertyValue,
    APIPlatformFlow,
    APIPlatformFlowCreateRequest,
    APIPlatformFlowPutRequest,
    APIPropertyBasedEnrollmentSchedule,
    APIRelativeDateTimeValue,
    APISignatureWebhookAuthSettings,
    APISingleConnectionAction,
    APISort,
    APIStaticAppendValue,
    APIStaticBranch,
    APIStaticBranchAction,
    APIStaticDateAnchor,
    APIStaticPropertyFilterDataSource,
    APIStaticTimeZoneStrategy,
    APIStaticValue,
    APITimeDelay,
    APITimeOfDay,
    APITimestampValue,
    APITimeWindow,
    APIUnEnrollmentSetting,
    APIWebhookAction,
    APIWeeklyEnrollmentSchedule,
    APIYearlyEnrollmentSchedule,
    BatchResponseAPIFlow,
    BatchResponseAPIFlowWithErrors,
    BatchResponseFlowIDWorkflowIDMappingResponse,
    BatchResponseFlowIDWorkflowIDMappingResponseWithErrors,
    CollectionResponseAPIFlowEmailCampaign,
    CollectionResponseAPIFlowListingForwardPaging,
    FlowIDWorkflowIDMappingResponse,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAdsSearchFilter,
    PublicAdsTimeFilter,
    PublicAllHistoryRefineBy,
    PublicAllPropertyTypesOperation,
    PublicAndFilterBranch,
    PublicAssociationFilterBranch,
    PublicAssociationInListFilter,
    PublicBoolPropertyOperation,
    PublicCalendarDatePropertyOperation,
    PublicCampaignInfluencedFilter,
    PublicCommunicationSubscriptionFilter,
    PublicComparativeDatePropertyOperation,
    PublicComparativePropertyUpdatedOperation,
    PublicConstantFilter,
    PublicCtaAnalyticsFilter,
    PublicDatePoint,
    PublicDatePropertyOperation,
    PublicDateTimePropertyOperation,
    PublicEmailEventFilter,
    PublicEmailSubscriptionFilter,
    PublicEnumerationPropertyOperation,
    PublicEventAnalyticsFilter,
    PublicEventFilterMetadata,
    PublicFiscalQuarterReference,
    PublicFiscalYearReference,
    PublicFormSubmissionFilter,
    PublicFormSubmissionOnPageFilter,
    PublicIndexedTimePoint,
    PublicIndexOffset,
    PublicInListFilter,
    PublicInListFilterMetadata,
    PublicIntegrationEventFilter,
    PublicMonthReference,
    PublicMultiStringPropertyOperation,
    PublicNotAllFilterBranch,
    PublicNotAnyFilterBranch,
    PublicNowReference,
    PublicNumAssociationsFilter,
    PublicNumberPropertyOperation,
    PublicNumOccurrencesRefineBy,
    PublicOrFilterBranch,
    PublicPageViewAnalyticsFilter,
    PublicPrivacyAnalyticsFilter,
    PublicPropertyAssociationFilterBranch,
    PublicPropertyAssociationInListFilter,
    PublicPropertyFilter,
    PublicPropertyReferencedTime,
    PublicQuarterReference,
    PublicRangedDatePropertyOperation,
    PublicRangedNumberPropertyOperation,
    PublicRangedTimeOperation,
    PublicRelativeComparativeTimestampRefineBy,
    PublicRelativeRangedTimestampRefineBy,
    PublicRestrictedFilterBranch,
    PublicRollingDateRangePropertyOperation,
    PublicRollingPropertyUpdatedOperation,
    PublicSetOccurrencesRefineBy,
    PublicStringPropertyOperation,
    PublicSurveyMonkeyFilter,
    PublicSurveyMonkeyValueFilter,
    PublicTimeOffset,
    PublicTimePointOperation,
    PublicTodayReference,
    PublicUnifiedEventsFilter,
    PublicUnifiedEventsFilterBranch,
    PublicWebinarFilter,
    PublicWeekReference,
    PublicYearReference,
)
```

# Cms

## Blogs

Types:

```python
from hubspot_sdk.types.cms import (
    AttachToLangPrimaryRequestVNext,
    BatchInputJsonNode,
    DetachFromLangGroupRequestVNext,
    SetNewLanguagePrimaryRequestVNext,
    UpdateLanguagesRequestVNext,
)
```

### Posts

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    Angle,
    BackgroundImage,
    BatchInputBlogPost,
    BatchResponseBlogPost,
    BatchResponseBlogPostWithErrors,
    BlogPost,
    BlogPostLanguageCloneRequestVNext,
    BreakpointStyles,
    CollectionResponseWithTotalBlogPostForwardPaging,
    CollectionResponseWithTotalVersionBlogPost,
    ColorStop,
    ContentCloneRequestVNext,
    ContentLanguageVariation,
    ContentScheduleRequestVNext,
    Gradient,
    LayoutSection,
    Margin,
    Padding,
    PublicAccessRule,
    RgbaColor,
    RowMetaData,
    SideOrCorner,
    Styles,
    VersionBlogPost,
)
```

Methods:

- <code title="post /cms/v3/blogs/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="patch /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">SyncPage[BlogPost]</a></code>
- <code title="delete /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/posts/multi-language/attach-to-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/posts/clone">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/create-language-variation">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/detach-from-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">get_draft_by_id</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">get_previous_version</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog_post.py">VersionBlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">get_previous_versions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_previous_versions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/collection_response_with_total_version_blog_post.py">CollectionResponseWithTotalVersionBlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/draft/push-live">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">push_live</a>(object_id) -> None</code>
- <code title="get /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">read</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/draft/reset">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">restore_previous_version</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">restore_previous_version_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/schedule">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/v3/blogs/posts/multi-language/set-new-lang-primary">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="patch /cms/v3/blogs/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/update-languages">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_langs_params.py">params</a>) -> None</code>

### Tags

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    BatchInputTag,
    BatchResponseTag,
    BatchResponseTagWithErrors,
    CollectionResponseWithTotalTagForwardPaging,
    Tag,
    TagCloneRequestVNext,
)
```

Methods:

- <code title="post /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="patch /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="get /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">SyncPage[Tag]</a></code>
- <code title="delete /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/archive">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">archive_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_archive_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/create">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/batch/read">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="put /cms/v3/blogs/tags/multi-language/set-new-lang-primary">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/update">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/update-languages">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_langs_params.py">params</a>) -> None</code>

## Domains

Types:

```python
from hubspot_sdk.types.cms import CollectionResponseWithTotalDomainForwardPaging, Domain
```

Methods:

- <code title="get /cms/v3/domains/">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/domain_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/domain.py">SyncPage[Domain]</a></code>
- <code title="get /cms/v3/domains/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">read</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/domain.py">Domain</a></code>

## Hubdb

Types:

```python
from hubspot_sdk.types.cms import (
    BatchInputHubDBTableRowBatchCloneRequest,
    BatchInputHubDBTableRowV3BatchUpdateRequest,
    BatchInputHubDBTableRowV3Request,
    BatchResponseHubDBTableRowV3,
    BatchResponseHubDBTableRowV3WithErrors,
    BoundedNextPage,
    BoundedPaging,
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
    Column,
    ColumnRequest,
    ForeignID,
    HubDBTableCloneRequest,
    HubDBTableRowBatchCloneRequest,
    HubDBTableRowV3,
    HubDBTableRowV3BatchUpdateRequest,
    HubDBTableRowV3Request,
    HubDBTableV3,
    HubDBTableV3Request,
    ImportResult,
    Option,
    RandomAccessCollectionResponseWithTotalHubDBTableRowV3,
    SimpleUser,
    StandardError,
    StreamingCollectionResponseWithTotalHubDBTableRowV3,
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
    Variant,
)
```

Methods:

- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">archive_table</a>(table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/create">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_table</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_table_row</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft/export">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">export_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_export_draft_table_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/export">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">export_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_export_table_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_all_draft_tables</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_all_draft_tables_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_hub_db_table_v3_forward_paging.py">CollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="get /cms/v3/hubdb/tables">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_all_tables</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_all_tables_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_hub_db_table_v3_forward_paging.py">CollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_draft_table_details_by_id</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_draft_table_details_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_draft_table_row_by_id</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_draft_table_row_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_details</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_details_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/unified_collection_response_with_total_base_hub_db_table_row_v3.py">UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/import">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">import_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_import_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/import_result.py">ImportResult</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">publish_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_publish_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">purge_draft_table_row</a>(row_id, \*, table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/purge">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">purge_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_purge_draft_table_rows_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/read">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">read_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_read_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/batch/read">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">read_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_read_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/versions/{versionId}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">remove_table_version</a>(version_id, \*, table_id_or_name) -> None</code>
- <code title="put /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">replace_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_replace_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">replace_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_replace_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">reset_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_reset_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/unpublish">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">unpublish_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_unpublish_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/update">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>

### Rows

Methods:

- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">create</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">list</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_params.py">params</a>) -> SyncPage[object]</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft/clone">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">clone_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">delete_draft</a>(row_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">get</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">get_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">list_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/unified_collection_response_with_total_base_hub_db_table_row_v3.py">UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3</a></code>
- <code title="put /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">replace_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_replace_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">update_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>

#### Draft

##### Batch

Methods:

- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/clone">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">clone_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_clone_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/create">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">create_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/purge">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">purge_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_purge_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/batch/read">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">read_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_read_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/read">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">read_draft_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_read_draft_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">replace_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_replace_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/update">client.cms.hubdb.rows.draft.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/draft/batch.py">update_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/draft/batch_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>

### Tables

Methods:

- <code title="post /cms/v3/hubdb/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">SyncPage[HubDBTableV3]</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">archive</a>(table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/clone">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">clone_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/versions/{versionId}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">delete_version</a>(version_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_draft_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/import">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">import_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_import_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/import_result.py">ImportResult</a></code>
- <code title="get /cms/v3/hubdb/tables/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list_drafts</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_drafts_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_hub_db_table_v3_forward_paging.py">CollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">publish_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_publish_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">reset_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_reset_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/unpublish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">unpublish</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_unpublish_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">update_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>

## URLRedirects

Types:

```python
from hubspot_sdk.types.cms import (
    CollectionResponseWithTotalURLMappingForwardPaging,
    URLMapping,
    URLMappingCreateRequestBody,
)
```

Methods:

- <code title="post /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="patch /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">update</a>(url_redirect_id, \*\*<a href="src/hubspot_sdk/types/cms/url_redirect_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="get /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">SyncPage[URLMapping]</a></code>
- <code title="delete /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">delete</a>(url_redirect_id) -> None</code>
- <code title="get /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">read</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>

# Conversations

## CustomChannels

Types:

```python
from hubspot_sdk.types.conversations import (
    ChannelIntegrationMessageEgg,
    ChannelIntegrationParticipant,
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
    CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging,
    ContactAddress,
    ContactAttachment,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactProfile,
    ContactURL,
    FileAttachment,
    LocationAttachment,
    MessageHeaderAttachment,
    PreResolvedContact,
    PreResolvedContacts,
    PublicChannelAccount,
    PublicChannelAccountEgg,
    PublicChannelAccountStagingToken,
    PublicChannelAccountStagingTokenUpdateRequest,
    PublicChannelAccountUpdateRequest,
    PublicChannelIntegrationChannel,
    PublicChannelIntegrationChannelCreate,
    PublicChannelIntegrationChannelPatch,
    PublicChannelIntegrationMessageUpdateRequest,
    PublicClient,
    PublicContact,
    PublicConversationsMessage,
    PublicDeliveryIdentifier,
    PublicFile,
    PublicLocation,
    PublicMessageFailureDetails,
    PublicMessageHeader,
    PublicMessageStatus,
    PublicQuickReplies,
    PublicRecipient,
    PublicSender,
    PublicSocialMetadataAttachment,
    PublicUnsupportedContent,
    PublicWhatsAppTemplateMetadata,
    QuickRepliesAttachment,
    QuickReply,
    SocialMetadata,
    SocialMetadataIntegrationAttachment,
    UnsupportedContentAttachment,
)
```

# CRM

Types:

```python
from hubspot_sdk.types import (
    AssociatedID,
    AssociationSpecWithLabel,
    BatchResponsePublicDefaultAssociation,
    CollectionResponseMultiAssociatedObjectWithLabel,
    CreatedResponseLabelsBetweenObjectPair,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    Option,
    Property,
    PropertyModificationMetadata,
    PublicDefaultAssociation,
)
```

## Associations

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPublicAssociation,
    BatchInputPublicObjectID,
    BatchResponsePublicAssociation,
    BatchResponsePublicAssociationMulti,
    PublicAssociation,
    PublicAssociationMulti,
)
```

Methods:

- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association.py">BatchResponsePublicAssociation</a></code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">read</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_multi.py">BatchResponsePublicAssociationMulti</a></code>

### V4

Types:

```python
from hubspot_sdk.types.crm.associations import (
    AssociationSpec1,
    AssociationSpecWithLabel1,
    BatchInputPublicAssociationMultiArchive,
    BatchInputPublicAssociationMultiPost,
    BatchInputPublicDefaultAssociationMultiPost,
    BatchInputPublicFetchAssociationsBatchRequest,
    BatchResponseLabelsBetweenObjectPair,
    BatchResponsePublicAssociationMultiWithLabel,
    BatchResponseVoid,
    DateTime,
    NextPage1,
    PreviousPage1,
    PublicAssociationMultiArchive,
    PublicAssociationMultiPost,
    PublicAssociationMultiWithLabel,
    PublicDefaultAssociationMultiPost,
    PublicFetchAssociationsBatchRequest,
    ReportCreationResponse,
    StandardError1,
)
```

Methods:

- <code title="put /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">create</a>(to_object_id, \*, object_type, object_id, to_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/created_response_labels_between_object_pair.py">CreatedResponseLabelsBetweenObjectPair</a></code>
- <code title="get /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">list</a>(to_object_type, \*, object_type, object_id, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/multi_associated_object_with_label.py">SyncPage[MultiAssociatedObjectWithLabel]</a></code>
- <code title="delete /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">delete</a>(to_object_id, \*, object_type, object_id, to_object_type) -> None</code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">archive_labels</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_archive_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="put /crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">create_default</a>(to_object_id, \*, from_object_type, from_object_id, to_object_type) -> <a href="./src/hubspot_sdk/types/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/v4/associations/usage/high-usage-report/{userId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">request</a>(user_id) -> <a href="./src/hubspot_sdk/types/crm/associations/report_creation_response.py">ReportCreationResponse</a></code>

## Extensions

### Calling

Types:

```python
from hubspot_sdk.types.crm.extensions import (
    ChannelConnectionSettingsPatchRequest,
    ChannelConnectionSettingsRequest,
    ChannelConnectionSettingsResponse,
    MarkRecordingAsReadyRequest,
    RecordingSettingsPatchRequest,
    RecordingSettingsRequest,
    RecordingSettingsResponse,
    SettingsPatchRequest,
    SettingsRequest,
    SettingsResponse,
)
```

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">get_url_format</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="post /crm/v3/extensions/calling/recordings/ready">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">mark_as_ready</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_mark_as_ready_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">read</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="post /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">register_url_format</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_register_url_format_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling.py">update_url_format</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_update_url_format_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>

## Objects

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputSimplePublicObjectBatchInput,
    BatchInputSimplePublicObjectBatchInputForCreate,
    BatchInputSimplePublicObjectBatchInputUpsert,
    BatchInputSimplePublicObjectID,
    BatchReadInputSimplePublicObjectID,
    BatchResponseSimplePublicObject,
    BatchResponseSimplePublicUpsertObject,
    CollectionResponseAssociatedID,
    CollectionResponseSimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
    CreatedResponseSimplePublicObject,
    Filter,
    FilterGroup,
    PublicAssociationsForObject,
    PublicGdprDeleteInput,
    PublicMergeInput,
    PublicObjectSearchRequest,
    SimplePublicObject,
    SimplePublicObjectBatchInput,
    SimplePublicObjectBatchInputForCreate,
    SimplePublicObjectBatchInputUpsert,
    SimplePublicObjectID,
    SimplePublicObjectInput,
    SimplePublicObjectInputForCreate,
    SimplePublicObjectWithAssociations,
    SimplePublicUpsertObject,
    ValueWithTimestamp,
)
```

### Companies

Methods:

- <code title="post /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/update">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="post /crm/v3/objects/companies/batch/archive">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/companies/merge">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">read</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/companies/search">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/upsert">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Contacts

Methods:

- <code title="post /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">update</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">delete</a>(contact_id) -> None</code>
- <code title="post /crm/v3/objects/contacts/merge">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/gdpr-delete">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">purge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_purge_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">read</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/contacts/search">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/contacts/batch/create">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/update">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/archive">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/contacts/batch/read">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/upsert">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Deals

Methods:

- <code title="post /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">update</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">delete</a>(deal_id) -> None</code>
- <code title="post /crm/v3/objects/0-3/merge">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">read</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-3/search">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/upsert">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Schemas

Types:

```python
from hubspot_sdk.types.crm.objects import (
    AssociationDefinition,
    AssociationDefinitionEgg,
    CollectionResponseObjectSchemaNoPaging,
    ObjectSchema,
    ObjectSchemaEgg,
    ObjectTypeDefinition,
    ObjectTypeDefinitionLabels,
    ObjectTypeDefinitionPatch,
    ObjectTypePropertyCreate,
    OptionInput,
)
```

Methods:

- <code title="post /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>
- <code title="patch /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/object_type_definition.py">ObjectTypeDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_delete_params.py">params</a>) -> None</code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}/associations/{associationIdentifier}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">archive_association</a>(association_identifier, \*, object_type) -> None</code>
- <code title="post /crm-object-schemas/v3/schemas/{objectType}/associations">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create_association</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/association_definition.py">AssociationDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">read</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>

## Owners

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePublicOwnerForwardPaging,
    PublicOwner,
    PublicTeam,
)
```

Methods:

- <code title="get /crm/v3/owners/">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/owner_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">SyncPage[PublicOwner]</a></code>
- <code title="get /crm/v3/owners/{ownerId}">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">get</a>(owner_id, \*\*<a href="src/hubspot_sdk/types/crm/owner_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">PublicOwner</a></code>

## Pipelines

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePipelineNoPaging,
    CollectionResponsePipelineStageNoPaging,
    CollectionResponsePublicAuditInfoNoPaging,
    Pipeline,
    PipelineInput,
    PipelinePatchInput,
    PipelineStage,
    PipelineStageInput,
    PipelineStagePatchInput,
    PublicAuditInfo,
)
```

Methods:

- <code title="post /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="patch /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="get /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_pipeline_no_paging.py">CollectionResponsePipelineNoPaging</a></code>
- <code title="delete /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">delete</a>(stage_id, \*, object_type, pipeline_id) -> None</code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/audit">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">get_audit</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_audit_info_no_paging.py">CollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">read</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="put /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">replace</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>

## Properties

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPropertyCreate,
    BatchInputPropertyName,
    BatchReadInputPropertyName,
    BatchResponseProperty,
    CollectionResponseProperty,
    CollectionResponsePropertyGroup,
    CreatedResponseProperty,
    CreatedResponsePropertyGroup,
    OptionInput,
    PropertyCreate,
    PropertyGroup,
    PropertyGroupCreate,
    PropertyGroupUpdate,
    PropertyName,
    PropertyUpdate,
)
```

Methods:

- <code title="post /crm/v3/properties/{objectType}/groups">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_property_group.py">CreatedResponsePropertyGroup</a></code>
- <code title="patch /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">update</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/property.py">Property</a></code>
- <code title="get /crm/v3/properties/{objectType}/groups">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property_group.py">CollectionResponsePropertyGroup</a></code>
- <code title="delete /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">delete</a>(property_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">get_by_name</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_get_by_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/property.py">Property</a></code>
- <code title="post /crm/v3/properties/{objectType}/batch/read">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">read</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_property.py">BatchResponseProperty</a></code>

# Files

Types:

```python
from hubspot_sdk.types import (
    CollectionResponseFile,
    CollectionResponseFolder,
    File,
    FileActionResponse,
    FileStat,
    FileUpdateInput,
    Folder,
    FolderActionResponse,
    FolderInput,
    FolderUpdateInput,
    FolderUpdateInputWithID,
    FolderUpdateTaskLocator,
    ImportFromURLInput,
    ImportFromURLTaskLocator,
    SignedURL,
)
```

## Files

Methods:

- <code title="patch /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">update</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/file.py">File</a></code>
- <code title="delete /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">delete</a>(file_id) -> None</code>
- <code title="delete /files/v3/files/{fileId}/gdpr-delete">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">gdpr_delete</a>(file_id) -> None</code>
- <code title="get /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/file.py">File</a></code>
- <code title="get /files/v3/files/stat/{path}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_by_path</a>(path, \*\*<a href="src/hubspot_sdk/types/files/file_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/file_stat.py">FileStat</a></code>
- <code title="get /files/v3/files/import-from-url/async/tasks/{taskId}/status">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_import_from_url_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/file_action_response.py">FileActionResponse</a></code>
- <code title="get /files/v3/files/{fileId}/signed-url">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_signed_url</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_signed_url_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/signed_url.py">SignedURL</a></code>
- <code title="post /files/v3/files/import-from-url/async">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">import_from_url_async</a>(\*\*<a href="src/hubspot_sdk/types/files/file_import_from_url_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/import_from_url_task_locator.py">ImportFromURLTaskLocator</a></code>
- <code title="put /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">replace</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/file.py">File</a></code>
- <code title="get /files/v3/files/search">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/file_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/collection_response_file.py">CollectionResponseFile</a></code>
- <code title="post /files/v3/files">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">upload</a>(\*\*<a href="src/hubspot_sdk/types/files/file_upload_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/file.py">File</a></code>

## Folders

Methods:

- <code title="post /files/v3/folders">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/folder.py">Folder</a></code>
- <code title="delete /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_id</a>(folder_id) -> None</code>
- <code title="delete /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_path</a>(folder_path) -> None</code>
- <code title="get /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/folder.py">Folder</a></code>
- <code title="get /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_path</a>(folder_path, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/folder.py">Folder</a></code>
- <code title="get /files/v3/folders/update/async/tasks/{taskId}/status">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_update_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/folder_action_response.py">FolderActionResponse</a></code>
- <code title="get /files/v3/folders/search">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/collection_response_folder.py">CollectionResponseFolder</a></code>
- <code title="post /files/v3/folders/update/async">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_async</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_update_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/folder_update_task_locator.py">FolderUpdateTaskLocator</a></code>
- <code title="patch /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_update_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/folder.py">Folder</a></code>

# Marketing

## Emails

Types:

```python
from hubspot_sdk.types.marketing import (
    AbTestCreateRequestVNext,
    AggregateEmailStatistics,
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
    CollectionResponseWithTotalPublicEmailForwardPaging,
    CollectionResponseWithTotalVersionPublicEmail,
    EmailCloneRequestVNext,
    EmailCreateRequest,
    EmailStatisticInterval,
    EmailStatisticsData,
    EmailUpdateRequest,
    Interval,
    Paging,
    PublicButtonStyleSettings,
    PublicDividerStyleSettings,
    PublicEmail,
    PublicEmailContent,
    PublicEmailFromDetails,
    PublicEmailRecipients,
    PublicEmailStyleSettings,
    PublicEmailSubscriptionDetails,
    PublicEmailTestingDetails,
    PublicEmailToDetails,
    PublicFontStyle,
    PublicRssEmailDetails,
    PublicWebversionDetails,
    SmartEmailField,
    VersionPublicEmail,
)
```

Methods:

- <code title="post /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="patch /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">SyncPage[PublicEmail]</a></code>
- <code title="delete /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">delete</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/emails/clone">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/ab-test/create-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/ab-test/get-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_ab_test_variation</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_draft</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/statistics/list">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_emails_list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_emails_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/aggregate_email_statistics.py">AggregateEmailStatistics</a></code>
- <code title="get /marketing/v3/emails/statistics/histogram">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_histogram</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_histogram_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_email_statistic_interval_no_paging.py">CollectionResponseWithTotalEmailStatisticIntervalNoPaging</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions/{revisionId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revision_by_id</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">VersionPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revisions</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_version_public_email.py">CollectionResponseWithTotalVersionPublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/publish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">publish_or_send</a>(email_id) -> None</code>
- <code title="get /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">read</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/draft/reset">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">reset_draft</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_draft_revision</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_revision</a>(revision_id, \*, email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/unpublish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">unpublish_or_cancel</a>(email_id) -> None</code>
- <code title="patch /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">upsert_draft</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_upsert_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>

## Forms

Types:

```python
from hubspot_sdk.types.marketing import (
    CollectionResponseFormDefinitionBaseForwardPaging,
    DatepickerField,
    DependentField,
    DependentFieldFilter,
    DropdownField,
    EmailField,
    EmailFieldValidation,
    EnumeratedFieldOption,
    FieldGroup,
    FileField,
    FormDefinitionBase,
    FormDefinitionCreateRequestBase,
    FormDisplayOptions,
    FormPostSubmitAction,
    FormStyle,
    HubSpotFormConfiguration,
    HubSpotFormDefinition,
    HubSpotFormDefinitionCreateRequest,
    HubSpotFormDefinitionPatchRequest,
    LegalConsentCheckbox,
    LegalConsentOptionsExplicitConsentToProcess,
    LegalConsentOptionsImplicitConsentToProcess,
    LegalConsentOptionsLegitimateInterest,
    LegalConsentOptionsNone,
    LifecycleStage,
    MobilePhoneField,
    MultiLineTextField,
    MultipleCheckboxesField,
    NumberField,
    NumberFieldValidation,
    PaymentLinkRadioField,
    PhoneField,
    PhoneFieldValidation,
    RadioField,
    SingleCheckboxField,
    SingleLineTextField,
)
```

Methods:

- <code title="post /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">create</a>() -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">HubSpotFormDefinition</a></code>
- <code title="patch /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">update</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">HubSpotFormDefinition</a></code>
- <code title="get /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/form_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">SyncPage[HubSpotFormDefinition]</a></code>
- <code title="delete /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">delete</a>(form_id) -> None</code>
- <code title="get /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">read</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">HubSpotFormDefinition</a></code>
- <code title="put /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">replace</a>(form_id) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">HubSpotFormDefinition</a></code>

## Subscriptions

Types:

```python
from hubspot_sdk.types.marketing import (
    PublicSubscriptionStatus,
    PublicSubscriptionStatusesResponse,
    PublicUpdateSubscriptionStatusRequest,
    SubscriptionDefinition,
    SubscriptionDefinitionsResponse,
)
```

Methods:

- <code title="get /communication-preferences/v3/definitions">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">list</a>() -> <a href="./src/hubspot_sdk/types/marketing/subscription_definitions_response.py">SubscriptionDefinitionsResponse</a></code>
- <code title="get /communication-preferences/v3/status/email/{emailAddress}">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">get_email_status</a>(email_address) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_statuses_response.py">PublicSubscriptionStatusesResponse</a></code>
- <code title="post /communication-preferences/v3/subscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">subscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_subscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/v3/unsubscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">unsubscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_unsubscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>

### V4

Types:

```python
from hubspot_sdk.types.marketing.subscriptions import (
    ActionResponseWithResultsPublicStatus,
    ActionResponseWithResultsPublicWideStatus,
    ActionResponseWithResultsSubscriptionDefinition,
    BatchInputPublicStatusRequest,
    BatchResponsePublicBulkOptOutFromAllResponse,
    BatchResponsePublicStatus,
    BatchResponsePublicStatusBulkResponse,
    BatchResponsePublicStatusBulkResponseWithErrors,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicWideStatusBulkResponseWithErrors,
    PartialPublicStatusRequest,
    PublicBulkOptOutFromAllResponse,
    PublicStatus,
    PublicStatusBulkResponse,
    PublicStatusRequest,
    PublicSubscriptionTranslation,
    PublicWideStatus,
    PublicWideStatusBulkResponse,
)
```

# Scheduler

## Meetings

Types:

```python
from hubspot_sdk.types.scheduler import (
    CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
    ExternalAssociationCreateRequest,
    ExternalBookingFormField,
    ExternalBookingInfo,
    ExternalBrandingMetadata,
    ExternalCalendarMeetingEventCreateProperties,
    ExternalCalendarMeetingEventCreateRequest,
    ExternalCalendarMeetingEventResponseProperties,
    ExternalCalenderMeetingEventResponse,
    ExternalClosedRange,
    ExternalCommunicationConsentCheckbox,
    ExternalEmailReminderSchedule,
    ExternalGuestSettings,
    ExternalLegalConsentOptions,
    ExternalLegalConsentResponse,
    ExternalLinkAvailability,
    ExternalLinkAvailabilityAndBusyTimes,
    ExternalLinkAvailabilityForDuration,
    ExternalLinkDisplayInfo,
    ExternalLinkFormField,
    ExternalLinkMetadata,
    ExternalMeetingAvailability,
    ExternalMeetingBooking,
    ExternalMeetingBookingResponse,
    ExternalMeetingsLinkSettings,
    ExternalMeetingsUser,
    ExternalMeetingsWelcomeScreenInfo,
    ExternalOption,
    ExternalReminder,
    ExternalTimeRange,
    ExternalUserBusyTimes,
    ExternalUserProfile,
    ExternalValidatedFormField,
)
```

# Settings

## Users

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicPermissionSetNoPaging,
    CollectionResponsePublicTeamNoPaging,
    CollectionResponsePublicUserForwardPaging,
    PublicPermissionSet,
    PublicTeam,
    PublicUser,
    PublicUserUpdate,
    UserProvisionRequest,
)
```

Methods:

- <code title="post /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">SyncPage[PublicUser]</a></code>
- <code title="delete /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">delete</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_delete_params.py">params</a>) -> None</code>
- <code title="get /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">read</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="put /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">replace</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>

# Webhooks

Types:

```python
from hubspot_sdk.types import (
    BatchInputSubscriptionBatchUpdateRequest,
    BatchResponseSubscriptionResponse,
    BatchResponseSubscriptionResponseWithErrors,
    SettingsChangeRequest,
    SettingsResponse,
    SubscriptionBatchUpdateRequest,
    SubscriptionCreateRequest,
    SubscriptionListResponse,
    SubscriptionPatchRequest,
    SubscriptionResponse,
    ThrottlingSettings,
)
```

Methods:

- <code title="post /webhooks/v3/{appId}/subscriptions">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/subscription_response.py">SubscriptionResponse</a></code>
- <code title="patch /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">update</a>(subscription_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/webhook_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/subscription_response.py">SubscriptionResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">delete</a>(subscription_id, \*, app_id) -> None</code>
- <code title="delete /webhooks/v3/{appId}/settings">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">clear</a>(app_id) -> None</code>
- <code title="put /webhooks/v3/{appId}/settings">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">configure</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_configure_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings_response.py">SettingsResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">read</a>(subscription_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/subscription_response.py">SubscriptionResponse</a></code>
- <code title="post /webhooks/v3/{appId}/subscriptions/batch/update">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">update_batch</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/batch_response_subscription_response.py">BatchResponseSubscriptionResponse</a></code>
