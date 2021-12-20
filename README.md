# Notebooks/utilities

## Upload su Icogen: get_sample_filenames.exe

Questo eseguibile consente di produrre un file batch.csv per la sottomissione a Icogen. L'eseguibile deve essere collocato nella **stessa cartella** dei file di sequenza (fastq.gz), dove sarà presente **anche** il file di esportazione del database FileMakerPro ottenuto con il pulsante **Esporta metadati Icogen** posto in basso a destra nel formato **dati_iris_giava**.

Per utilizzare l'eseguibile, è necessario cliccarci due volte sopra. Nota: il file batch.csv, se già presente, sarà sovrascritto.

Una volta creato il file batch.csv, selezionare tutti i file di sequenza e il file batch.csv e creare un archivio in formato **zip** (NO 7zip o altri formati!), cliccando col pulsante destro sui file selezionati e selezionando "Aggiungi ad archivio".

Il file zip così creato andrà caricato sul server Icogen accedendovi con le credenziali nella cartella MEGA `Covid/icogen`. Istruzioni dettagliate per questa operazione sono contenute nel paragrafo "Modalità del trasferimento ftps" a pagina 25 del documento IRIDA21-ICoGen.pdf, contenuto in questa repository.
