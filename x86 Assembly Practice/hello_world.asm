; hello_world.asm
;
; Author: Jordan Dominick
; Date: 9/20/21

global _start

section .text:
_start:

    ; main function

    mov eax, 0x4             ; use the write syscall
    mov ebx, 1               ; use stdout as the fd
    mov ecx, message         ; use the message as the buffer
    mov edx, message_length  ; and supply the length
    int 0x80                 ; invoke the syscall

    mov eax, 0x1             ; use the exit syscall
    mov ebx, 0               ; set the exit status to 0
    int 0x80                 ; invoke the syscall

    mov eax, 0x4             ; use the uname syscall
    mov ebx, 1               ; use stdout as the fd
    mov ecx, message2        ; use the message as the buffer
    mov edx, message2_length ; and supply the length
    int 0x80                 ; invoke the syscall

    ; exit function

    mov eax, 0x1             ; use the exit syscall
    mov ebx, 0               ; set the exit status to 0
    int 0x80                 ; invoke the syscall



section .data:
    message: db "This Program Was Written In Assembly", 0xA ; defines the variable "message"
    message2: db "Why do i hate myself?", 0xA                     ; defines the path for mkdir to write to
    message_length equ $-message                            ; calculates the message length
    message2_length equ $-message2