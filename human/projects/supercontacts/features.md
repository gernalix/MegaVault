# SuperContacts Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `app/src/main/java/com/supercontacts/app/MainActivity.kt`: MainActivity, onCreate, onNewIntent
- `app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt`: SuperContactsApp, ContactListScreen, selectHomeSort, loadPatchVersion, EmojiToolbarButton, HomeSortStatus, HomeSortDialog, homeSortLabel
- `app/src/main/java/com/supercontacts/app/data/backup/BackupModels.kt`: BackupState
- `app/src/main/java/com/supercontacts/app/data/backup/BackupPreferencesStore.kt`: BackupPreferencesStore, readFolderUri, writeFolderUri, clearFolderUri, readAutoExportEnabled, writeAutoExportEnabled, readLastExportAt, writeLastExportAt
- `app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt`: PreparedImport, SuperContactsBackupManager, notifyDatabaseChanged, setBackupFolder, setAutoExportEnabled, exportNow, importFromUri, importFromBackupFolder
- `app/src/main/java/com/supercontacts/app/data/local/BackupMetadataEntity.kt`: BackupMetadataEntity
- `app/src/main/java/com/supercontacts/app/data/local/ContactEntity.kt`: ContactEntity
- `app/src/main/java/com/supercontacts/app/data/local/ContactEventEntity.kt`: ContactEventEntity
- `app/src/main/java/com/supercontacts/app/data/local/ContactFieldEntity.kt`: ContactFieldEntity
- `app/src/main/java/com/supercontacts/app/data/local/ContactInitiativeEntity.kt`: ContactInitiativeEntity
- `app/src/main/java/com/supercontacts/app/data/local/ContactsDao.kt`: ContactsDao, insertContact, updateContact, deleteContact, insertField, insertEvent, insertInitiative, insertTag
- `app/src/main/java/com/supercontacts/app/data/local/SuperContactsDatabase.kt`: SuperContactsDatabase, contactsDao, getInstance, openTemporary, closeInstance, canMigrateFrom, buildDatabase, migrate
- `app/src/main/java/com/supercontacts/app/data/local/TagEntity.kt`: TagEntity
- `app/src/main/java/com/supercontacts/app/data/repository/AddressAutocompleteRepository.kt`: AddressSuggestion, ResolvedAddress, AddressSuggestionSource, AddressAutocompleteRepository, search, resolve, resetSession, client
- `app/src/main/java/com/supercontacts/app/data/repository/AppContainer.kt`: AppContainer, contactsRepository, addressAutocompleteRepository, contactPhotoStore, backupManager, homePreferencesStore, database, closeDataLayer
- `app/src/main/java/com/supercontacts/app/data/repository/ContactDuplicateModels.kt`: ContactDuplicateCandidate, ContactDuplicateReason
- `app/src/main/java/com/supercontacts/app/data/repository/ContactDuplicateNormalizer.kt`: ContactDuplicateNormalizer, normalizePhone, normalizeEmail, normalizeLinkOrUsername, normalizeLooseText, phoneMatches, looseTextMatches, firstTokenPrefix
- `app/src/main/java/com/supercontacts/app/data/repository/ContactFieldType.kt`: ContactFieldType
- `app/src/main/java/com/supercontacts/app/data/repository/ContactInput.kt`: ContactInput, hasAnyValue
- `app/src/main/java/com/supercontacts/app/data/repository/ContactModels.kt`: ContactSummary, ContactSearchMatch, ContactFieldSuggestion, ContactPhotoReference, ContactTag, ContactFieldTimestamp, ContactFieldDescriptor, ContactEvent
- `app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoStore.kt`: ContactPhotoCropSpec, BitmapCrop, ContactPhotoStore, loadPreviewBitmap, saveCroppedPhoto, migrateLegacyPhotoToSaf, deletePhoto, loadPhotoBitmap
- `app/src/main/java/com/supercontacts/app/data/repository/ContactsRepository.kt`: DuplicateLinkValue, ContactsRepository, EventEntityType, EventActionType, listContacts, searchContacts, filterContacts, getContactsByTag

## Confini operativi
- app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(null)
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewModel.removeTagFromContact(contactId, tagId) },
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:660:private fun ContactListScreen(
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:897:private suspend fun loadPatchVersion(context: Context): String =
- app/src/main/AndroidManifest.xml:1:<?xml version="1.0" encoding="utf-8"?>
- app/src/main/AndroidManifest.xml:10:android:allowBackup="false"
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:193:backupManager = AppContainer.backupManager(context),
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:199:val patchVersion by produceState(initialValue = "", context) {
