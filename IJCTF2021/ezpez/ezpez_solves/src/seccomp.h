#ifndef SECCOMP_H
#define SECCOMP_H

#include <stddef.h>
#include <stdlib.h>
#include <sys/prctl.h>
#include <sys/syscall.h>

#include <linux/filter.h>
#include <linux/seccomp.h>
#include <linux/audit.h>

#define Allow(syscall) \
    BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, SYS_##syscall, 0, 1), \
    BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_ALLOW)

#define ArchField offsetof(struct seccomp_data, arch)

struct sock_filter filter[17];

struct sock_fprog filterprog;

void sandbox();

#endif
