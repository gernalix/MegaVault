# surface-recovery-hardening Roadmap

## Now
- Lasciare `rsync-transfer.service` in esecuzione e monitorare log, kernel e Kuma.
- Mantenere persistenti solo watchdog, Kuma push, adaptive throttle e automount destinazione.
- Osservare che il filtro watchdog non ripeta pause su eventi USB non-storage.

## Next
- Valutare un helper documentato per montare la source BitLocker read-only se il mapping deve essere ripetuto spesso.
- Aggiungere smoke test shell per `verify-mapping` con output `findmnt` multilinea.

## Later
- Razionalizzare report legacy e backup non tracciati solo su richiesta esplicita.
