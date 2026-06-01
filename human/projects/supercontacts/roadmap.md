# SuperContacts Roadmap

## Segnali dal codice
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:382:onNextMonth = viewModel::nextHistoryMonth,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2027:onNextMonth: () -> Unit,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2062:onNextMonth = onNextMonth,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2197:onNextMonth: () -> Unit,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2231:onNextMonth = onNextMonth,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:2264:onNextMonth: () -> Unit,
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:403:copyPhotoDocuments(sourcePhotos, targetPhotos)
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:431:private fun copyPhotoDocuments(
- app/src/main/java/com/supercontacts/app/data/backup/SuperContactsBackupManager.kt:722:while (cursor.moveToNext()) {
- app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoStore.kt:163:val ratio = ceil(largestSide.toDouble() / maxSizePx.toDouble()).roundToInt()
- app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoStore.kt:265:val document = resolvePhotoDocument(
- app/src/main/java/com/supercontacts/app/data/repository/ContactPhotoStore.kt:284:val document = resolvePhotoDocument(

## Debito/rischi da considerare
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:180:import kotlinx.coroutines.withTimeoutOrNull
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:348:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:362:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:364:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:417:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:422:onErrorDismiss = viewModel::clearError,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:449:viewModel.clearError()
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:463:errorMessage = uiState.errorMessage,
- app/src/main/java/com/supercontacts/app/MainActivity.kt:15:private var latestIntent by mutableStateOf<Intent?>(null)
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:439:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:487:onDeleteUnusedPhoto = viewModel::deleteUnusedContactPhoto,
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:551:onDelete = { contactId ->
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:552:viewModel.deleteContact(contactId) {
- app/src/main/java/com/supercontacts/app/ui/app/SuperContactsApp.kt:567:onRemoveTag = { contactId, tagId -> viewModel.removeTagFromContact(contactId, tagId) },
