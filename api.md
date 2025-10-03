# Shared Types

```python
from hubspot_sdk.types import (
    BatchInputString,
    Error,
    ErrorDetail,
    ForwardPaging,
    NextPage,
    Paging,
    PreviousPage,
    StandardError,
)
```

# Account

Types:

```python
from hubspot_sdk.types import (
    AccountActingUser,
    AccountCollectionResponseHydratedCriticalActionForwardPaging,
    AccountCollectionResponsePublicAPIUserActionEventForwardPaging,
    AccountCollectionResponsePublicLoginAuditForwardPaging,
    AccountHydratedCriticalAction,
    AccountPublicAPIUserActionEvent,
    AccountPublicLoginAudit,
)
```

## Info

Types:

```python
from hubspot_sdk.types.account import (
    AccountInfoAPIUsage,
    AccountInfoCollectionResponseAPIUsage,
    AccountInfoPortalInformationResponse,
)
```

# Auth

## OAuth

Types:

```python
from hubspot_sdk.types.auth import (
    AuthOAuthAccessTokenInfoResponse,
    AuthOAuthRefreshTokenInfoResponse,
    AuthOAuthTokenResponseIf,
)
```

Methods:

- <code title="post /oauth/v1/token">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">create</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/auth_oauth_token_response_if.py">AuthOAuthTokenResponseIf</a></code>
- <code title="delete /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">delete</a>(token) -> None</code>
- <code title="get /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get</a>(token) -> <a href="./src/hubspot_sdk/types/auth/auth_oauth_refresh_token_info_response.py">AuthOAuthRefreshTokenInfoResponse</a></code>

# Automation

Types:

```python
from hubspot_sdk.types import (
    AutomationAPIAbTestBranchAction,
    AutomationAPIActionDataValue,
    AutomationAPIAppendObjectPropertyValue,
    AutomationAPIAssociationDataSource,
    AutomationAPIAssociationTimestampDataSource,
    AutomationAPIAuthKeyWebhookAuthSettings,
    AutomationAPIBlockedDate,
    AutomationAPIConnection,
    AutomationAPIContactFlow,
    AutomationAPIContactFlowCreateRequest,
    AutomationAPIContactFlowPutRequest,
    AutomationAPIContactPropertyAnchor,
    AutomationAPICustomCodeAction,
    AutomationAPIDailyEnrollmentSchedule,
    AutomationAPIDatasetFieldPropertyFilterDataSource,
    AutomationAPIEnrolledArgumentPropertyFilterDataSource,
    AutomationAPIEnrolledRecordPropertyFilterDataSource,
    AutomationAPIEnrollmentEventPropertyValue,
    AutomationAPIEnumerationOutputField,
    AutomationAPIEventBasedEnrollmentCriteria,
    AutomationAPIFetchedObjectPropertyValue,
    AutomationAPIFlow,
    AutomationAPIFlowBatchFetchFlowIDCoordinate,
    AutomationAPIFlowBatchFetchMigrationFlowIDCoordinate,
    AutomationAPIFlowBatchFetchMigrationWorkflowIDCoordinate,
    AutomationAPIFlowBatchInput,
    AutomationAPIFlowBatchMigrationInput,
    AutomationAPIFlowCreateRequest,
    AutomationAPIFlowEmailCampaign,
    AutomationAPIFlowListing,
    AutomationAPIFlowPutRequest,
    AutomationAPIIncrementValue,
    AutomationAPIInputVariable,
    AutomationAPIListBasedEnrollmentCriteria,
    AutomationAPIListBranch,
    AutomationAPIListBranchAction,
    AutomationAPIManualEnrollmentCriteria,
    AutomationAPIMonthlyRelativeDaysEnrollmentSchedule,
    AutomationAPIMonthlySpecificDaysEnrollmentSchedule,
    AutomationAPIObjectPropertyValue,
    AutomationAPIPlatformFlow,
    AutomationAPIPlatformFlowCreateRequest,
    AutomationAPIPlatformFlowPutRequest,
    AutomationAPIPropertyBasedEnrollmentSchedule,
    AutomationAPIRelativeDateTimeValue,
    AutomationAPISignatureWebhookAuthSettings,
    AutomationAPISingleConnectionAction,
    AutomationAPISort,
    AutomationAPIStaticAppendValue,
    AutomationAPIStaticBranch,
    AutomationAPIStaticBranchAction,
    AutomationAPIStaticDateAnchor,
    AutomationAPIStaticPropertyFilterDataSource,
    AutomationAPIStaticTimeZoneStrategy,
    AutomationAPIStaticValue,
    AutomationAPITimeDelay,
    AutomationAPITimeOfDay,
    AutomationAPITimestampValue,
    AutomationAPITimeWindow,
    AutomationAPIUnEnrollmentSetting,
    AutomationAPIWebhookAction,
    AutomationAPIWeeklyEnrollmentSchedule,
    AutomationAPIYearlyEnrollmentSchedule,
    AutomationBatchResponseAPIFlow,
    AutomationBatchResponseAPIFlowWithErrors,
    AutomationBatchResponseFlowIDWorkflowIDMappingResponse,
    AutomationBatchResponseFlowIDWorkflowIDMappingResponseWithErrors,
    AutomationCollectionResponseAPIFlowEmailCampaign,
    AutomationCollectionResponseAPIFlowListingForwardPaging,
    AutomationFlowIDWorkflowIDMappingResponse,
    AutomationPublicAbsoluteComparativeTimestampRefineBy,
    AutomationPublicAbsoluteRangedTimestampRefineBy,
    AutomationPublicAdsSearchFilter,
    AutomationPublicAdsTimeFilter,
    AutomationPublicAllHistoryRefineBy,
    AutomationPublicAllPropertyTypesOperation,
    AutomationPublicAndFilterBranch,
    AutomationPublicAssociationFilterBranch,
    AutomationPublicAssociationInListFilter,
    AutomationPublicBoolPropertyOperation,
    AutomationPublicCalendarDatePropertyOperation,
    AutomationPublicCampaignInfluencedFilter,
    AutomationPublicCommunicationSubscriptionFilter,
    AutomationPublicComparativeDatePropertyOperation,
    AutomationPublicComparativePropertyUpdatedOperation,
    AutomationPublicConstantFilter,
    AutomationPublicCtaAnalyticsFilter,
    AutomationPublicDatePoint,
    AutomationPublicDatePropertyOperation,
    AutomationPublicDateTimePropertyOperation,
    AutomationPublicEmailEventFilter,
    AutomationPublicEmailSubscriptionFilter,
    AutomationPublicEnumerationPropertyOperation,
    AutomationPublicEventAnalyticsFilter,
    AutomationPublicEventFilterMetadata,
    AutomationPublicFiscalQuarterReference,
    AutomationPublicFiscalYearReference,
    AutomationPublicFormSubmissionFilter,
    AutomationPublicFormSubmissionOnPageFilter,
    AutomationPublicIndexedTimePoint,
    AutomationPublicIndexOffset,
    AutomationPublicInListFilter,
    AutomationPublicInListFilterMetadata,
    AutomationPublicIntegrationEventFilter,
    AutomationPublicMonthReference,
    AutomationPublicMultiStringPropertyOperation,
    AutomationPublicNotAllFilterBranch,
    AutomationPublicNotAnyFilterBranch,
    AutomationPublicNowReference,
    AutomationPublicNumAssociationsFilter,
    AutomationPublicNumberPropertyOperation,
    AutomationPublicNumOccurrencesRefineBy,
    AutomationPublicOrFilterBranch,
    AutomationPublicPageViewAnalyticsFilter,
    AutomationPublicPrivacyAnalyticsFilter,
    AutomationPublicPropertyAssociationFilterBranch,
    AutomationPublicPropertyAssociationInListFilter,
    AutomationPublicPropertyFilter,
    AutomationPublicPropertyReferencedTime,
    AutomationPublicQuarterReference,
    AutomationPublicRangedDatePropertyOperation,
    AutomationPublicRangedNumberPropertyOperation,
    AutomationPublicRangedTimeOperation,
    AutomationPublicRelativeComparativeTimestampRefineBy,
    AutomationPublicRelativeRangedTimestampRefineBy,
    AutomationPublicRestrictedFilterBranch,
    AutomationPublicRollingDateRangePropertyOperation,
    AutomationPublicRollingPropertyUpdatedOperation,
    AutomationPublicSetOccurrencesRefineBy,
    AutomationPublicStringPropertyOperation,
    AutomationPublicSurveyMonkeyFilter,
    AutomationPublicSurveyMonkeyValueFilter,
    AutomationPublicTimeOffset,
    AutomationPublicTimePointOperation,
    AutomationPublicTodayReference,
    AutomationPublicUnifiedEventsFilter,
    AutomationPublicUnifiedEventsFilterBranch,
    AutomationPublicWebinarFilter,
    AutomationPublicWeekReference,
    AutomationPublicYearReference,
)
```

## Actions

Types:

```python
from hubspot_sdk.types.automation import (
    AutomationActionsBatchInputCallbackCompletionBatchRequest,
    AutomationActionsCallbackCompletionBatchRequest,
    AutomationActionsCallbackCompletionRequest,
    AutomationActionsCollectionResponsePublicActionDefinitionForwardPaging,
    AutomationActionsCollectionResponsePublicActionFunctionIdentifierNoPaging,
    AutomationActionsCollectionResponsePublicActionRevisionForwardPaging,
    AutomationActionsFieldTypeDefinition,
    AutomationActionsInputFieldDefinition,
    AutomationActionsOption,
    AutomationActionsOutputFieldDefinition,
    AutomationActionsPublicActionDefinition,
    AutomationActionsPublicActionDefinitionEgg,
    AutomationActionsPublicActionDefinitionPatch,
    AutomationActionsPublicActionFunction,
    AutomationActionsPublicActionFunctionIdentifier,
    AutomationActionsPublicActionLabels,
    AutomationActionsPublicActionRevision,
    AutomationActionsPublicConditionalSingleFieldDependency,
    AutomationActionsPublicExecutionTranslationRule,
    AutomationActionsPublicObjectRequestOptions,
    AutomationActionsPublicSingleFieldDependency,
)
```

Methods:

- <code title="post /automation/v4/actions/{appId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_definition.py">AutomationActionsPublicActionDefinition</a></code>
- <code title="patch /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">update</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_definition.py">AutomationActionsPublicActionDefinition</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_collection_response_public_action_revision_forward_paging.py">AutomationActionsCollectionResponsePublicActionRevisionForwardPaging</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">archive_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="post /automation/v4/actions/callbacks/{callbackId}/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete</a>(callback_id, \*\*<a href="src/hubspot_sdk/types/automation/action_complete_params.py">params</a>) -> None</code>
- <code title="post /automation/v4/actions/callbacks/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete_batch</a>(\*\*<a href="src/hubspot_sdk/types/automation/action_complete_batch_params.py">params</a>) -> None</code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_function_identifier.py">AutomationActionsPublicActionFunctionIdentifier</a></code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_function_identifier.py">AutomationActionsPublicActionFunctionIdentifier</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_function.py">AutomationActionsPublicActionFunction</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">read</a>(function_id, \*, app_id, definition_id, function_type) -> <a href="./src/hubspot_sdk/types/automation/automation_actions_public_action_function.py">AutomationActionsPublicActionFunction</a></code>

# Cms

Types:

```python
from hubspot_sdk.types import (
    CmsCollectionResponseWithTotalURLMappingForwardPaging,
    CmsURLMapping,
    CmsURLMappingCreateRequestBody,
)
```

## Blogs

### Tags

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    CmsBlogsTagsAttachToLangPrimaryRequestVNext,
    CmsBlogsTagsBatchInputJsonNode,
    CmsBlogsTagsBatchInputTag,
    CmsBlogsTagsBatchResponseTag,
    CmsBlogsTagsBatchResponseTagWithErrors,
    CmsBlogsTagsCollectionResponseWithTotalTagForwardPaging,
    CmsBlogsTagsDetachFromLangGroupRequestVNext,
    CmsBlogsTagsSetNewLanguagePrimaryRequestVNext,
    CmsBlogsTagsTag,
    CmsBlogsTagsTagCloneRequestVNext,
    CmsBlogsTagsUpdateLanguagesRequestVNext,
)
```

Methods:

- <code title="post /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_tag.py">CmsBlogsTagsTag</a></code>
- <code title="patch /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_tag.py">CmsBlogsTagsTag</a></code>
- <code title="get /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_collection_response_with_total_tag_forward_paging.py">CmsBlogsTagsCollectionResponseWithTotalTagForwardPaging</a></code>
- <code title="delete /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/archive">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">archive_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_archive_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/create">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_batch_response_tag.py">CmsBlogsTagsBatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_tag.py">CmsBlogsTagsTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_tag.py">CmsBlogsTagsTag</a></code>
- <code title="post /cms/v3/blogs/tags/batch/read">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_batch_response_tag.py">CmsBlogsTagsBatchResponseTag</a></code>
- <code title="put /cms/v3/blogs/tags/multi-language/set-new-lang-primary">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/update">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/cms_blogs_tags_batch_response_tag.py">CmsBlogsTagsBatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/update-languages">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_langs_params.py">params</a>) -> None</code>

## Domains

Types:

```python
from hubspot_sdk.types.cms import (
    CmsDomainsCollectionResponseWithTotalDomainForwardPaging,
    CmsDomainsDomain,
)
```

Methods:

- <code title="get /cms/v3/domains/">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/domain_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_domains_collection_response_with_total_domain_forward_paging.py">CmsDomainsCollectionResponseWithTotalDomainForwardPaging</a></code>
- <code title="get /cms/v3/domains/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">read</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/cms_domains_domain.py">CmsDomainsDomain</a></code>

## Hubdb

Types:

```python
from hubspot_sdk.types.cms import (
    CmsHubdbBatchInputHubDBTableRowBatchCloneRequest,
    CmsHubdbBatchInputHubDBTableRowV3BatchUpdateRequest,
    CmsHubdbBatchInputHubDBTableRowV3Request,
    CmsHubdbBatchResponseHubDBTableRowV3,
    CmsHubdbBatchResponseHubDBTableRowV3WithErrors,
    CmsHubdbBoundedNextPage,
    CmsHubdbBoundedPaging,
    CmsHubdbCollectionResponseWithTotalHubDBTableV3ForwardPaging,
    CmsHubdbColumn,
    CmsHubdbColumnRequest,
    CmsHubdbForeignID,
    CmsHubdbHubDBTableCloneRequest,
    CmsHubdbHubDBTableRowBatchCloneRequest,
    CmsHubdbHubDBTableRowV3,
    CmsHubdbHubDBTableRowV3BatchUpdateRequest,
    CmsHubdbHubDBTableRowV3Request,
    CmsHubdbHubDBTableV3,
    CmsHubdbHubDBTableV3Request,
    CmsHubdbImportResult,
    CmsHubdbOption,
    CmsHubdbRandomAccessCollectionResponseWithTotalHubDBTableRowV3,
    CmsHubdbSimpleUser,
    CmsHubdbStandardError,
    CmsHubdbStreamingCollectionResponseWithTotalHubDBTableRowV3,
    CmsHubdbUnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
    CmsHubdbVariant,
)
```

Methods:

- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">archive_table</a>(table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/clone">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">clone_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_clone_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/create">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_table</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">create_table_row</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_create_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft/export">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">export_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_export_draft_table_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/export">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">export_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_export_table_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_all_draft_tables</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_all_draft_tables_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_collection_response_with_total_hub_db_table_v3_forward_paging.py">CmsHubdbCollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="get /cms/v3/hubdb/tables">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_all_tables</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_all_tables_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_collection_response_with_total_hub_db_table_v3_forward_paging.py">CmsHubdbCollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_draft_table_details_by_id</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_draft_table_details_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_draft_table_row_by_id</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_draft_table_row_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_details</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_details_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">get_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_get_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_unified_collection_response_with_total_base_hub_db_table_row_v3.py">CmsHubdbUnifiedCollectionResponseWithTotalBaseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/import">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">import_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_import_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_import_result.py">CmsHubdbImportResult</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">publish_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_publish_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">purge_draft_table_row</a>(row_id, \*, table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/purge">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">purge_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_purge_draft_table_rows_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/read">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">read_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_read_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/batch/read">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">read_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_read_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/versions/{versionId}">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">remove_table_version</a>(version_id, \*, table_id_or_name) -> None</code>
- <code title="put /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">replace_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_replace_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">replace_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_replace_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">reset_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_reset_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/unpublish">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">unpublish_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_unpublish_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_v3.py">CmsHubdbHubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table_row</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_row_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_hub_db_table_row_v3.py">CmsHubdbHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/update">client.cms.hubdb.<a href="./src/hubspot_sdk/resources/cms/hubdb/hubdb.py">update_draft_table_rows</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb_update_draft_table_rows_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>

### Rows

#### Batch

Methods:

- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">replace</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cms_hubdb_batch_response_hub_db_table_row_v3.py">CmsHubdbBatchResponseHubDBTableRowV3</a></code>

## URLRedirects

Methods:

- <code title="post /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms_url_mapping.py">CmsURLMapping</a></code>
- <code title="patch /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">update</a>(url_redirect_id, \*\*<a href="src/hubspot_sdk/types/cms/url_redirect_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms_url_mapping.py">CmsURLMapping</a></code>
- <code title="get /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms_collection_response_with_total_url_mapping_forward_paging.py">CmsCollectionResponseWithTotalURLMappingForwardPaging</a></code>
- <code title="delete /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">delete</a>(url_redirect_id) -> None</code>
- <code title="get /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">read</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms_url_mapping.py">CmsURLMapping</a></code>

# CRM

Types:

```python
from hubspot_sdk.types import (
    CRMAssociatedID,
    CRMAssociationDefinition,
    CRMAssociationDefinitionEgg,
    CRMAssociationSpec,
    CRMAssociationSpecWithLabel,
    CRMBatchResponsePublicDefaultAssociation,
    CRMCollectionResponseMultiAssociatedObjectWithLabel,
    CRMCollectionResponseObjectSchemaNoPaging,
    CRMCreatedResponseLabelsBetweenObjectPair,
    CRMLabelsBetweenObjectPair,
    CRMMultiAssociatedObjectWithLabel,
    CRMObjectSchema,
    CRMObjectSchemaEgg,
    CRMObjectTypeDefinition,
    CRMObjectTypeDefinitionLabels,
    CRMObjectTypeDefinitionPatch,
    CRMObjectTypePropertyCreate,
    CRMOption,
    CRMOptionInput,
    CRMProperty,
    CRMPropertyModificationMetadata,
    CRMPublicDefaultAssociation,
    CRMPublicObjectID,
)
```

## Associations

Types:

```python
from hubspot_sdk.types.crm import (
    CRMAssociationsBatchInputPublicAssociation,
    CRMAssociationsBatchInputPublicObjectID,
    CRMAssociationsBatchResponsePublicAssociation,
    CRMAssociationsBatchResponsePublicAssociationMulti,
    CRMAssociationsPublicAssociation,
    CRMAssociationsPublicAssociationMulti,
)
```

Methods:

- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_associations_batch_response_public_association.py">CRMAssociationsBatchResponsePublicAssociation</a></code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">read</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_associations_batch_response_public_association_multi.py">CRMAssociationsBatchResponsePublicAssociationMulti</a></code>

### V4

Types:

```python
from hubspot_sdk.types.crm.associations import (
    CRMAssociationsV4AssociationSpec1,
    CRMAssociationsV4AssociationSpecWithLabel1,
    CRMAssociationsV4BatchInputPublicAssociationMultiArchive,
    CRMAssociationsV4BatchInputPublicAssociationMultiPost,
    CRMAssociationsV4BatchInputPublicDefaultAssociationMultiPost,
    CRMAssociationsV4BatchInputPublicFetchAssociationsBatchRequest,
    CRMAssociationsV4BatchResponseLabelsBetweenObjectPair,
    CRMAssociationsV4BatchResponsePublicAssociationMultiWithLabel,
    CRMAssociationsV4BatchResponseVoid,
    CRMAssociationsV4DateTime,
    CRMAssociationsV4NextPage1,
    CRMAssociationsV4PreviousPage1,
    CRMAssociationsV4PublicAssociationMultiArchive,
    CRMAssociationsV4PublicAssociationMultiPost,
    CRMAssociationsV4PublicAssociationMultiWithLabel,
    CRMAssociationsV4PublicDefaultAssociationMultiPost,
    CRMAssociationsV4PublicFetchAssociationsBatchRequest,
    CRMAssociationsV4ReportCreationResponse,
    CRMAssociationsV4StandardError1,
)
```

Methods:

- <code title="put /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">create</a>(to_object_id, \*, object_type, object_id, to_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_created_response_labels_between_object_pair.py">CRMCreatedResponseLabelsBetweenObjectPair</a></code>
- <code title="get /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">list</a>(to_object_type, \*, object_type, object_id, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_collection_response_multi_associated_object_with_label.py">CRMCollectionResponseMultiAssociatedObjectWithLabel</a></code>
- <code title="delete /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">delete</a>(to_object_id, \*, object_type, object_id, to_object_type) -> None</code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">archive_labels</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_archive_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/crm_associations_v4_batch_response_void.py">CRMAssociationsV4BatchResponseVoid</a></code>
- <code title="put /crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">create_default</a>(to_object_id, \*, from_object_type, from_object_id, to_object_type) -> <a href="./src/hubspot_sdk/types/crm_batch_response_public_default_association.py">CRMBatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/v4/associations/usage/high-usage-report/{userId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4.py">request</a>(user_id) -> <a href="./src/hubspot_sdk/types/crm/associations/crm_associations_v4_report_creation_response.py">CRMAssociationsV4ReportCreationResponse</a></code>

## Extensions

### Calling

Types:

```python
from hubspot_sdk.types.crm.extensions import (
    CRMExtensionsCallingChannelConnectionSettingsPatchRequest,
    CRMExtensionsCallingChannelConnectionSettingsRequest,
    CRMExtensionsCallingChannelConnectionSettingsResponse,
    CRMExtensionsCallingMarkRecordingAsReadyRequest,
    CRMExtensionsCallingRecordingSettingsPatchRequest,
    CRMExtensionsCallingRecordingSettingsRequest,
    CRMExtensionsCallingRecordingSettingsResponse,
    CRMExtensionsCallingSettingsPatchRequest,
    CRMExtensionsCallingSettingsRequest,
    CRMExtensionsCallingSettingsResponse,
)
```

#### ChannelConnectionSettings

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/channel_connection_setting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_channel_connection_settings_response.py">CRMExtensionsCallingChannelConnectionSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/channel_connection_setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_channel_connection_settings_response.py">CRMExtensionsCallingChannelConnectionSettingsResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_channel_connection_settings_response.py">CRMExtensionsCallingChannelConnectionSettingsResponse</a></code>

#### RecordingSettings

Methods:

- <code title="get /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">get_url_format</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_recording_settings_response.py">CRMExtensionsCallingRecordingSettingsResponse</a></code>
- <code title="post /crm/v3/extensions/calling/recordings/ready">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">mark_as_ready</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_mark_as_ready_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">register_url_format</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_register_url_format_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_recording_settings_response.py">CRMExtensionsCallingRecordingSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">update_url_format</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_update_url_format_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/crm_extensions_calling_recording_settings_response.py">CRMExtensionsCallingRecordingSettingsResponse</a></code>

#### Settings

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/setting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_settings_response.py">WebhooksSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_settings_response.py">WebhooksSettingsResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks_settings_response.py">WebhooksSettingsResponse</a></code>

## Objects

Types:

```python
from hubspot_sdk.types.crm import (
    CRMObjectsBatchInputSimplePublicObjectBatchInput,
    CRMObjectsBatchInputSimplePublicObjectBatchInputForCreate,
    CRMObjectsBatchInputSimplePublicObjectBatchInputUpsert,
    CRMObjectsBatchInputSimplePublicObjectID,
    CRMObjectsBatchReadInputSimplePublicObjectID,
    CRMObjectsBatchResponseSimplePublicObject,
    CRMObjectsBatchResponseSimplePublicUpsertObject,
    CRMObjectsCollectionResponseAssociatedID,
    CRMObjectsCollectionResponseSimplePublicObjectWithAssociations,
    CRMObjectsCollectionResponseWithTotalSimplePublicObject,
    CRMObjectsCreatedResponseSimplePublicObject,
    CRMObjectsFilter,
    CRMObjectsFilterGroup,
    CRMObjectsPublicAssociationsForObject,
    CRMObjectsPublicGdprDeleteInput,
    CRMObjectsPublicMergeInput,
    CRMObjectsPublicObjectSearchRequest,
    CRMObjectsSimplePublicObject,
    CRMObjectsSimplePublicObjectBatchInput,
    CRMObjectsSimplePublicObjectBatchInputForCreate,
    CRMObjectsSimplePublicObjectBatchInputUpsert,
    CRMObjectsSimplePublicObjectID,
    CRMObjectsSimplePublicObjectInput,
    CRMObjectsSimplePublicObjectInputForCreate,
    CRMObjectsSimplePublicObjectWithAssociations,
    CRMObjectsSimplePublicUpsertObject,
    CRMObjectsValueWithTimestamp,
)
```

### Companies

Methods:

- <code title="post /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_created_response_simple_public_object.py">CRMObjectsCreatedResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/update">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_batch_response_simple_public_object.py">CRMObjectsBatchResponseSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_simple_public_object_with_associations.py">CRMObjectsCollectionResponseSimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/companies/batch/archive">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/companies/merge">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object.py">CRMObjectsSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">read</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object_with_associations.py">CRMObjectsSimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/companies/search">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_with_total_simple_public_object.py">CRMObjectsCollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/upsert">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_batch_response_simple_public_upsert_object.py">CRMObjectsBatchResponseSimplePublicUpsertObject</a></code>

### Contacts

Methods:

- <code title="post /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_created_response_simple_public_object.py">CRMObjectsCreatedResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/update">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_batch_response_simple_public_object.py">CRMObjectsBatchResponseSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_simple_public_object_with_associations.py">CRMObjectsCollectionResponseSimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/contacts/batch/archive">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/contacts/merge">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object.py">CRMObjectsSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/gdpr-delete">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">purge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_purge_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">read</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object_with_associations.py">CRMObjectsSimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/contacts/search">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_with_total_simple_public_object.py">CRMObjectsCollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/upsert">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_batch_response_simple_public_upsert_object.py">CRMObjectsBatchResponseSimplePublicUpsertObject</a></code>

### Deals

Methods:

- <code title="post /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_created_response_simple_public_object.py">CRMObjectsCreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">update</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object.py">CRMObjectsSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_simple_public_object_with_associations.py">CRMObjectsCollectionResponseSimplePublicObjectWithAssociations</a></code>
- <code title="delete /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">delete</a>(deal_id) -> None</code>
- <code title="post /crm/v3/objects/0-3/merge">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object.py">CRMObjectsSimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">read</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_simple_public_object_with_associations.py">CRMObjectsSimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-3/search">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_collection_response_with_total_simple_public_object.py">CRMObjectsCollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/upsert">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_objects_batch_response_simple_public_upsert_object.py">CRMObjectsBatchResponseSimplePublicUpsertObject</a></code>

### Schemas

Methods:

- <code title="post /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_object_schema.py">CRMObjectSchema</a></code>
- <code title="patch /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_object_type_definition.py">CRMObjectTypeDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_collection_response_object_schema_no_paging.py">CRMCollectionResponseObjectSchemaNoPaging</a></code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_delete_params.py">params</a>) -> None</code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}/associations/{associationIdentifier}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">archive_association</a>(association_identifier, \*, object_type) -> None</code>
- <code title="post /crm-object-schemas/v3/schemas/{objectType}/associations">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create_association</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_association_definition.py">CRMAssociationDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">read</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm_object_schema.py">CRMObjectSchema</a></code>

## Pipelines

Types:

```python
from hubspot_sdk.types.crm import (
    CRMPipelinesCollectionResponsePipelineNoPaging,
    CRMPipelinesCollectionResponsePipelineStageNoPaging,
    CRMPipelinesCollectionResponsePublicAuditInfoNoPaging,
    CRMPipelinesPipeline,
    CRMPipelinesPipelineInput,
    CRMPipelinesPipelinePatchInput,
    CRMPipelinesPipelineStage,
    CRMPipelinesPipelineStageInput,
    CRMPipelinesPipelineStagePatchInput,
    CRMPipelinesPublicAuditInfo,
)
```

Methods:

- <code title="post /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_pipeline.py">CRMPipelinesPipeline</a></code>
- <code title="patch /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_pipeline_stage.py">CRMPipelinesPipelineStage</a></code>
- <code title="get /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_collection_response_pipeline_no_paging.py">CRMPipelinesCollectionResponsePipelineNoPaging</a></code>
- <code title="delete /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">delete</a>(stage_id, \*, object_type, pipeline_id) -> None</code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/audit">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">get_audit</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_collection_response_public_audit_info_no_paging.py">CRMPipelinesCollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">read</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_pipeline_stage.py">CRMPipelinesPipelineStage</a></code>
- <code title="put /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">replace</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_pipelines_pipeline_stage.py">CRMPipelinesPipelineStage</a></code>

## Properties

Types:

```python
from hubspot_sdk.types.crm import (
    CRMPropertiesBatchInputPropertyCreate,
    CRMPropertiesBatchInputPropertyName,
    CRMPropertiesBatchReadInputPropertyName,
    CRMPropertiesBatchResponseProperty,
    CRMPropertiesCollectionResponseProperty,
    CRMPropertiesCollectionResponsePropertyGroup,
    CRMPropertiesCreatedResponseProperty,
    CRMPropertiesCreatedResponsePropertyGroup,
    CRMPropertiesOptionInput,
    CRMPropertiesPropertyCreate,
    CRMPropertiesPropertyGroup,
    CRMPropertiesPropertyGroupCreate,
    CRMPropertiesPropertyGroupUpdate,
    CRMPropertiesPropertyName,
    CRMPropertiesPropertyUpdate,
)
```

Methods:

- <code title="post /crm/v3/properties/{objectType}/groups">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_properties_created_response_property_group.py">CRMPropertiesCreatedResponsePropertyGroup</a></code>
- <code title="patch /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">update</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_property.py">CRMProperty</a></code>
- <code title="get /crm/v3/properties/{objectType}/groups">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/crm_properties_collection_response_property_group.py">CRMPropertiesCollectionResponsePropertyGroup</a></code>
- <code title="delete /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">delete</a>(property_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">get_by_name</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_get_by_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm_property.py">CRMProperty</a></code>
- <code title="post /crm/v3/properties/{objectType}/batch/read">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties.py">read</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/crm_properties_batch_response_property.py">CRMPropertiesBatchResponseProperty</a></code>

# Files

Types:

```python
from hubspot_sdk.types import (
    FilesCollectionResponseFile,
    FilesCollectionResponseFolder,
    FilesFile,
    FilesFileActionResponse,
    FilesFileStat,
    FilesFileUpdateInput,
    FilesFolder,
    FilesFolderActionResponse,
    FilesFolderInput,
    FilesFolderUpdateInput,
    FilesFolderUpdateInputWithID,
    FilesFolderUpdateTaskLocator,
    FilesImportFromURLInput,
    FilesImportFromURLTaskLocator,
    FilesSignedURL,
)
```

## Files

Methods:

- <code title="patch /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">update</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_file.py">FilesFile</a></code>
- <code title="delete /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">delete</a>(file_id) -> None</code>
- <code title="delete /files/v3/files/{fileId}/gdpr-delete">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">gdpr_delete</a>(file_id) -> None</code>
- <code title="get /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_file.py">FilesFile</a></code>
- <code title="get /files/v3/files/stat/{path}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_by_path</a>(path, \*\*<a href="src/hubspot_sdk/types/files/file_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_file_stat.py">FilesFileStat</a></code>
- <code title="get /files/v3/files/import-from-url/async/tasks/{taskId}/status">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_import_from_url_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files_file_action_response.py">FilesFileActionResponse</a></code>
- <code title="get /files/v3/files/{fileId}/signed-url">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_signed_url</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_signed_url_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_signed_url.py">FilesSignedURL</a></code>
- <code title="post /files/v3/files/import-from-url/async">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">import_from_url_async</a>(\*\*<a href="src/hubspot_sdk/types/files/file_import_from_url_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_import_from_url_task_locator.py">FilesImportFromURLTaskLocator</a></code>
- <code title="put /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">replace</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_file.py">FilesFile</a></code>
- <code title="get /files/v3/files/search">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/file_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_collection_response_file.py">FilesCollectionResponseFile</a></code>
- <code title="post /files/v3/files">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">upload</a>(\*\*<a href="src/hubspot_sdk/types/files/file_upload_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_file.py">FilesFile</a></code>

## Folders

Methods:

- <code title="post /files/v3/folders">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_folder.py">FilesFolder</a></code>
- <code title="delete /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_id</a>(folder_id) -> None</code>
- <code title="delete /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_path</a>(folder_path) -> None</code>
- <code title="get /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_folder.py">FilesFolder</a></code>
- <code title="get /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_path</a>(folder_path, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_folder.py">FilesFolder</a></code>
- <code title="get /files/v3/folders/update/async/tasks/{taskId}/status">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_update_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files_folder_action_response.py">FilesFolderActionResponse</a></code>
- <code title="get /files/v3/folders/search">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_collection_response_folder.py">FilesCollectionResponseFolder</a></code>
- <code title="post /files/v3/folders/update/async">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_async</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_update_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_folder_update_task_locator.py">FilesFolderUpdateTaskLocator</a></code>
- <code title="patch /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_update_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files_folder.py">FilesFolder</a></code>

# Marketing

## Emails

Types:

```python
from hubspot_sdk.types.marketing import (
    MarketingEmailsAbTestCreateRequestVNext,
    MarketingEmailsAggregateEmailStatistics,
    MarketingEmailsCollectionResponseWithTotalEmailStatisticIntervalNoPaging,
    MarketingEmailsCollectionResponseWithTotalPublicEmailForwardPaging,
    MarketingEmailsCollectionResponseWithTotalVersionPublicEmail,
    MarketingEmailsEmailCloneRequestVNext,
    MarketingEmailsEmailCreateRequest,
    MarketingEmailsEmailStatisticInterval,
    MarketingEmailsEmailStatisticsData,
    MarketingEmailsEmailUpdateRequest,
    MarketingEmailsInterval,
    MarketingEmailsPaging,
    MarketingEmailsPublicButtonStyleSettings,
    MarketingEmailsPublicDividerStyleSettings,
    MarketingEmailsPublicEmail,
    MarketingEmailsPublicEmailContent,
    MarketingEmailsPublicEmailFromDetails,
    MarketingEmailsPublicEmailRecipients,
    MarketingEmailsPublicEmailStyleSettings,
    MarketingEmailsPublicEmailSubscriptionDetails,
    MarketingEmailsPublicEmailTestingDetails,
    MarketingEmailsPublicEmailToDetails,
    MarketingEmailsPublicFontStyle,
    MarketingEmailsPublicRssEmailDetails,
    MarketingEmailsPublicWebversionDetails,
    MarketingEmailsSmartEmailField,
    MarketingEmailsVersionPublicEmail,
    MarketingEmailsVersionUser,
)
```

Methods:

- <code title="post /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="patch /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="get /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_collection_response_with_total_public_email_forward_paging.py">MarketingEmailsCollectionResponseWithTotalPublicEmailForwardPaging</a></code>
- <code title="delete /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">delete</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/emails/clone">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="post /marketing/v3/emails/ab-test/create-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/ab-test/get-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_ab_test_variation</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_draft</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="get /marketing/v3/emails/statistics/list">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_emails_list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_emails_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_aggregate_email_statistics.py">MarketingEmailsAggregateEmailStatistics</a></code>
- <code title="get /marketing/v3/emails/statistics/histogram">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_histogram</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_histogram_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_collection_response_with_total_email_statistic_interval_no_paging.py">MarketingEmailsCollectionResponseWithTotalEmailStatisticIntervalNoPaging</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions/{revisionId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revision_by_id</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_version_public_email.py">MarketingEmailsVersionPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revisions</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_collection_response_with_total_version_public_email.py">MarketingEmailsCollectionResponseWithTotalVersionPublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/publish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">publish_or_send</a>(email_id) -> None</code>
- <code title="get /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">read</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/draft/reset">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">reset_draft</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_draft_revision</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_revision</a>(revision_id, \*, email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/unpublish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">unpublish_or_cancel</a>(email_id) -> None</code>
- <code title="patch /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">upsert_draft</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_upsert_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_emails_public_email.py">MarketingEmailsPublicEmail</a></code>

## Forms

Types:

```python
from hubspot_sdk.types.marketing import (
    MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging,
    MarketingFormsDatepickerField,
    MarketingFormsDependentField,
    MarketingFormsDependentFieldFilter,
    MarketingFormsDropdownField,
    MarketingFormsEmailField,
    MarketingFormsEmailFieldValidation,
    MarketingFormsEnumeratedFieldOption,
    MarketingFormsFieldGroup,
    MarketingFormsFileField,
    MarketingFormsFormDefinitionBase,
    MarketingFormsFormDefinitionCreateRequestBase,
    MarketingFormsFormDisplayOptions,
    MarketingFormsFormPostSubmitAction,
    MarketingFormsFormStyle,
    MarketingFormsHubSpotFormConfiguration,
    MarketingFormsHubSpotFormDefinition,
    MarketingFormsHubSpotFormDefinitionCreateRequest,
    MarketingFormsHubSpotFormDefinitionPatchRequest,
    MarketingFormsLegalConsentCheckbox,
    MarketingFormsLegalConsentOptionsExplicitConsentToProcess,
    MarketingFormsLegalConsentOptionsImplicitConsentToProcess,
    MarketingFormsLegalConsentOptionsLegitimateInterest,
    MarketingFormsLegalConsentOptionsNone,
    MarketingFormsLifecycleStage,
    MarketingFormsMobilePhoneField,
    MarketingFormsMultiLineTextField,
    MarketingFormsMultipleCheckboxesField,
    MarketingFormsNumberField,
    MarketingFormsNumberFieldValidation,
    MarketingFormsPaymentLinkRadioField,
    MarketingFormsPhoneField,
    MarketingFormsPhoneFieldValidation,
    MarketingFormsRadioField,
    MarketingFormsSingleCheckboxField,
    MarketingFormsSingleLineTextField,
)
```

Methods:

- <code title="post /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">create</a>() -> <a href="./src/hubspot_sdk/types/marketing/marketing_forms_form_definition_base.py">object</a></code>
- <code title="patch /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">update</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_forms_form_definition_base.py">object</a></code>
- <code title="get /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/form_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_forms_collection_response_form_definition_base_forward_paging.py">MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging</a></code>
- <code title="delete /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">delete</a>(form_id) -> None</code>
- <code title="get /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">read</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_forms_form_definition_base.py">object</a></code>
- <code title="put /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">replace</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_forms_form_definition_base.py">object</a></code>

## Subscriptions

Types:

```python
from hubspot_sdk.types.marketing import (
    MarketingSubscriptionsActionResponseWithResultsPublicStatus,
    MarketingSubscriptionsActionResponseWithResultsPublicWideStatus,
    MarketingSubscriptionsActionResponseWithResultsSubscriptionDefinition,
    MarketingSubscriptionsBatchInputPublicStatusRequest,
    MarketingSubscriptionsBatchResponsePublicBulkOptOutFromAllResponse,
    MarketingSubscriptionsBatchResponsePublicStatus,
    MarketingSubscriptionsBatchResponsePublicStatusBulkResponse,
    MarketingSubscriptionsBatchResponsePublicStatusBulkResponseWithErrors,
    MarketingSubscriptionsBatchResponsePublicWideStatusBulkResponse,
    MarketingSubscriptionsBatchResponsePublicWideStatusBulkResponseWithErrors,
    MarketingSubscriptionsPartialPublicStatusRequest,
    MarketingSubscriptionsPublicBulkOptOutFromAllResponse,
    MarketingSubscriptionsPublicStatus,
    MarketingSubscriptionsPublicStatusBulkResponse,
    MarketingSubscriptionsPublicStatusRequest,
    MarketingSubscriptionsPublicSubscriptionTranslation,
    MarketingSubscriptionsPublicWideStatus,
    MarketingSubscriptionsPublicWideStatusBulkResponse,
    MarketingSubscriptionsSubscriptionDefinition,
)
```

Methods:

- <code title="get /communication-preferences/v3/definitions">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">list</a>() -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/marketing_subscriptions_v3_subscription_definitions_response.py">MarketingSubscriptionsV3SubscriptionDefinitionsResponse</a></code>
- <code title="get /communication-preferences/v3/status/email/{emailAddress}">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">get_email_status</a>(email_address) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/marketing_subscriptions_v3_public_subscription_statuses_response.py">MarketingSubscriptionsV3PublicSubscriptionStatusesResponse</a></code>
- <code title="post /communication-preferences/v3/subscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">subscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_subscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/marketing_subscriptions_v3_public_subscription_status.py">MarketingSubscriptionsV3PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/v3/unsubscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">unsubscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_unsubscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/marketing_subscriptions_v3_public_subscription_status.py">MarketingSubscriptionsV3PublicSubscriptionStatus</a></code>

### V3

Types:

```python
from hubspot_sdk.types.marketing.subscriptions import (
    MarketingSubscriptionsV3PublicSubscriptionStatus,
    MarketingSubscriptionsV3PublicSubscriptionStatusesResponse,
    MarketingSubscriptionsV3PublicUpdateSubscriptionStatusRequest,
    MarketingSubscriptionsV3SubscriptionDefinitionsResponse,
)
```

# Webhooks

Types:

```python
from hubspot_sdk.types import (
    WebhooksBatchInputSubscriptionBatchUpdateRequest,
    WebhooksBatchResponseSubscriptionResponse,
    WebhooksBatchResponseSubscriptionResponseWithErrors,
    WebhooksSettingsChangeRequest,
    WebhooksSettingsResponse,
    WebhooksSubscriptionBatchUpdateRequest,
    WebhooksSubscriptionCreateRequest,
    WebhooksSubscriptionListResponse,
    WebhooksSubscriptionPatchRequest,
    WebhooksSubscriptionResponse,
    WebhooksThrottlingSettings,
)
```

Methods:

- <code title="post /webhooks/v3/{appId}/subscriptions">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_subscription_response.py">WebhooksSubscriptionResponse</a></code>
- <code title="patch /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">update</a>(subscription_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/webhook_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_subscription_response.py">WebhooksSubscriptionResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks_subscription_list_response.py">WebhooksSubscriptionListResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">delete</a>(subscription_id, \*, app_id) -> None</code>
- <code title="delete /webhooks/v3/{appId}/settings">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">clear</a>(app_id) -> None</code>
- <code title="put /webhooks/v3/{appId}/settings">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">configure</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_configure_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_settings_response.py">WebhooksSettingsResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">read</a>(subscription_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/webhooks_subscription_response.py">WebhooksSubscriptionResponse</a></code>
- <code title="post /webhooks/v3/{appId}/subscriptions/batch/update">client.webhooks.<a href="./src/hubspot_sdk/resources/webhooks.py">update_batch</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhook_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_batch_response_subscription_response.py">WebhooksBatchResponseSubscriptionResponse</a></code>
