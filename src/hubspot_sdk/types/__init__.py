# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import marketing
from .. import _compat
from .shared import (
    Error as Error,
    Paging as Paging,
    NextPage as NextPage,
    ErrorDetail as ErrorDetail,
    PreviousPage as PreviousPage,
    ForwardPaging as ForwardPaging,
    StandardError as StandardError,
    BatchInputString as BatchInputString,
)
from .crm_option import CRMOption as CRMOption
from .files_file import FilesFile as FilesFile
from .crm_property import CRMProperty as CRMProperty
from .files_folder import FilesFolder as FilesFolder
from .cms_url_mapping import CmsURLMapping as CmsURLMapping
from .files_file_stat import FilesFileStat as FilesFileStat
from .crm_option_param import CRMOptionParam as CRMOptionParam
from .file_read_params import FileReadParams as FileReadParams
from .files_signed_url import FilesSignedURL as FilesSignedURL
from .crm_associated_id import CRMAssociatedID as CRMAssociatedID
from .crm_object_schema import CRMObjectSchema as CRMObjectSchema
from .file_create_params import FileCreateParams as FileCreateParams
from .file_search_params import FileSearchParams as FileSearchParams
from .file_upload_params import FileUploadParams as FileUploadParams
from .file_replace_params import FileReplaceParams as FileReplaceParams
from .crm_public_object_id import CRMPublicObjectID as CRMPublicObjectID
from .webhook_create_params import WebhookCreateParams as WebhookCreateParams
from .webhook_update_params import WebhookUpdateParams as WebhookUpdateParams
from .file_get_by_path_params import FileGetByPathParams as FileGetByPathParams
from .file_get_metadata_params import FileGetMetadataParams as FileGetMetadataParams
from .webhook_configure_params import WebhookConfigureParams as WebhookConfigureParams
from .crm_association_definition import CRMAssociationDefinition as CRMAssociationDefinition
from .crm_association_spec_param import CRMAssociationSpecParam as CRMAssociationSpecParam
from .crm_object_type_definition import CRMObjectTypeDefinition as CRMObjectTypeDefinition
from .crm_public_object_id_param import CRMPublicObjectIDParam as CRMPublicObjectIDParam
from .file_get_signed_url_params import FileGetSignedURLParams as FileGetSignedURLParams
from .files_file_action_response import FilesFileActionResponse as FilesFileActionResponse
from .webhooks_settings_response import WebhooksSettingsResponse as WebhooksSettingsResponse
from .file_import_from_url_params import FileImportFromURLParams as FileImportFromURLParams
from .webhook_update_batch_params import WebhookUpdateBatchParams as WebhookUpdateBatchParams
from .files_folder_action_response import FilesFolderActionResponse as FilesFolderActionResponse
from .webhooks_throttling_settings import WebhooksThrottlingSettings as WebhooksThrottlingSettings
from .file_update_properties_params import FileUpdatePropertiesParams as FileUpdatePropertiesParams
from .crm_labels_between_object_pair import CRMLabelsBetweenObjectPair as CRMLabelsBetweenObjectPair
from .crm_public_default_association import CRMPublicDefaultAssociation as CRMPublicDefaultAssociation
from .files_collection_response_file import FilesCollectionResponseFile as FilesCollectionResponseFile
from .webhooks_subscription_response import WebhooksSubscriptionResponse as WebhooksSubscriptionResponse
from .files_folder_update_task_locator import FilesFolderUpdateTaskLocator as FilesFolderUpdateTaskLocator
from .crm_object_type_definition_labels import CRMObjectTypeDefinitionLabels as CRMObjectTypeDefinitionLabels
from .crm_property_modification_metadata import CRMPropertyModificationMetadata as CRMPropertyModificationMetadata
from .files_import_from_url_task_locator import FilesImportFromURLTaskLocator as FilesImportFromURLTaskLocator
from .webhooks_throttling_settings_param import WebhooksThrottlingSettingsParam as WebhooksThrottlingSettingsParam
from .webhooks_subscription_list_response import WebhooksSubscriptionListResponse as WebhooksSubscriptionListResponse
from .crm_object_type_property_create_param import CRMObjectTypePropertyCreateParam as CRMObjectTypePropertyCreateParam
from .crm_multi_associated_object_with_label import (
    CRMMultiAssociatedObjectWithLabel as CRMMultiAssociatedObjectWithLabel,
)
from .crm_object_type_definition_labels_param import (
    CRMObjectTypeDefinitionLabelsParam as CRMObjectTypeDefinitionLabelsParam,
)
from .file_update_properties_recursively_params import (
    FileUpdatePropertiesRecursivelyParams as FileUpdatePropertiesRecursivelyParams,
)
from .crm_batch_response_public_default_association import (
    CRMBatchResponsePublicDefaultAssociation as CRMBatchResponsePublicDefaultAssociation,
)
from .webhooks_batch_response_subscription_response import (
    WebhooksBatchResponseSubscriptionResponse as WebhooksBatchResponseSubscriptionResponse,
)
from .crm_collection_response_object_schema_no_paging import (
    CRMCollectionResponseObjectSchemaNoPaging as CRMCollectionResponseObjectSchemaNoPaging,
)
from .crm_created_response_labels_between_object_pair import (
    CRMCreatedResponseLabelsBetweenObjectPair as CRMCreatedResponseLabelsBetweenObjectPair,
)
from .webhooks_subscription_batch_update_request_param import (
    WebhooksSubscriptionBatchUpdateRequestParam as WebhooksSubscriptionBatchUpdateRequestParam,
)
from .crm_collection_response_multi_associated_object_with_label import (
    CRMCollectionResponseMultiAssociatedObjectWithLabel as CRMCollectionResponseMultiAssociatedObjectWithLabel,
)
from .cms_collection_response_with_total_url_mapping_forward_paging import (
    CmsCollectionResponseWithTotalURLMappingForwardPaging as CmsCollectionResponseWithTotalURLMappingForwardPaging,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    marketing.marketing_forms_collection_response_form_definition_base_forward_paging.MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging.update_forward_refs()  # type: ignore
    marketing.marketing_forms_datepicker_field.MarketingFormsDatepickerField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_dependent_field.MarketingFormsDependentField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_dropdown_field.MarketingFormsDropdownField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_email_field.MarketingFormsEmailField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_field_group.MarketingFormsFieldGroup.update_forward_refs()  # type: ignore
    marketing.marketing_forms_file_field.MarketingFormsFileField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_hub_spot_form_definition.MarketingFormsHubSpotFormDefinition.update_forward_refs()  # type: ignore
    marketing.marketing_forms_mobile_phone_field.MarketingFormsMobilePhoneField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_multi_line_text_field.MarketingFormsMultiLineTextField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_multiple_checkboxes_field.MarketingFormsMultipleCheckboxesField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_number_field.MarketingFormsNumberField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_payment_link_radio_field.MarketingFormsPaymentLinkRadioField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_phone_field.MarketingFormsPhoneField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_radio_field.MarketingFormsRadioField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_single_checkbox_field.MarketingFormsSingleCheckboxField.update_forward_refs()  # type: ignore
    marketing.marketing_forms_single_line_text_field.MarketingFormsSingleLineTextField.update_forward_refs()  # type: ignore
else:
    marketing.marketing_forms_collection_response_form_definition_base_forward_paging.MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_datepicker_field.MarketingFormsDatepickerField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_dependent_field.MarketingFormsDependentField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_dropdown_field.MarketingFormsDropdownField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_email_field.MarketingFormsEmailField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_field_group.MarketingFormsFieldGroup.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_file_field.MarketingFormsFileField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_hub_spot_form_definition.MarketingFormsHubSpotFormDefinition.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_mobile_phone_field.MarketingFormsMobilePhoneField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_multi_line_text_field.MarketingFormsMultiLineTextField.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_multiple_checkboxes_field.MarketingFormsMultipleCheckboxesField.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_number_field.MarketingFormsNumberField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_payment_link_radio_field.MarketingFormsPaymentLinkRadioField.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_phone_field.MarketingFormsPhoneField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_radio_field.MarketingFormsRadioField.model_rebuild(_parent_namespace_depth=0)
    marketing.marketing_forms_single_checkbox_field.MarketingFormsSingleCheckboxField.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.marketing_forms_single_line_text_field.MarketingFormsSingleLineTextField.model_rebuild(
        _parent_namespace_depth=0
    )
