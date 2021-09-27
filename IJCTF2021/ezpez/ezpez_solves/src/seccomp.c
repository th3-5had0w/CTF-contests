#include"seccomp.h"

struct sock_filter filter[] = {
    /* validate arch */
    BPF_STMT(BPF_LD+BPF_W+BPF_ABS, ArchField),
    BPF_JUMP( BPF_JMP+BPF_JEQ+BPF_K, AUDIT_ARCH_X86_64, 1, 0),
    BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_KILL),

    /* load syscall */
    BPF_STMT(BPF_LD+BPF_W+BPF_ABS, offsetof(struct seccomp_data, nr)),

    /* list of allowed syscalls */
    Allow(exit_group),
    Allow(read),
    Allow(write),
    Allow(close),
    Allow(brk),
    Allow(fstat),

    /* and if we don't match above, die */
    // BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_TRAP),
    BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_KILL),
};

struct sock_fprog filterprog = {
    .len = sizeof(filter)/sizeof(filter[0]),
    .filter = filter
};

void sandbox(){
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) exit(EXIT_FAILURE);
    if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &filterprog) == -1)exit(EXIT_FAILURE);
}
