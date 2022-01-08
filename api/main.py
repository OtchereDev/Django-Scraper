from .firebase.firestoreConfig import uploadToFireStore
from .remoteok.pageFetcher import getJobsRemoteOk
from .weworkremote.pageFetcher import getjobsWeWorkRemotely

def getJobs():
    all_jobs = []
    remoteok = getJobsRemoteOk()
    weworkremotely = getjobsWeWorkRemotely()
    all_jobs += remoteok
    all_jobs+=weworkremotely

    current_size, chunk_size = 0, 490
    while True:
        uploadToFireStore(all_jobs[current_size:current_size+chunk_size])
        current_size += 490

        if current_size >= len(all_jobs):
            break;
    print(f"Successfull add {len(all_jobs)} jobs")
