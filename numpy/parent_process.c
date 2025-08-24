#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid;

    printf("Parent process started. PID: %d\n", getpid());

    pid = fork();  // Create a new process

    if (pid < 0) {
        // Fork failed
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process
        printf("Child process. PID: %d, Parent PID: %d\n", getpid(), getppid());
        exit(0);
    } else {
        // Parent process
        printf("Parent process continuing. PID: %d, Child PID: %d\n", getpid(), pid);
        sleep(1); // Give child time to run
    }

    printf("Parent process ending. PID: %d\n", getpid());

    return 0;
}
