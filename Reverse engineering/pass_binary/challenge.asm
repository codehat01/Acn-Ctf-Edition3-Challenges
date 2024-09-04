section .data
    ; Obfuscated flag data
    flag_part1 db 0xEA, 0x85, 0xD1, 0xE2, 0xC2, 0xD1, 0xDA, 0xE4 ; Encrypted "ACN_CTF{"
    flag_part2 db 0xF6, 0xF0, 0xC3, 0xC0, 0xE7, 0xF0, 0xC3, 0xE4 ; Encrypted "d3c0d3_7"
    flag_part3 db 0xE4, 0xF0, 0xC7, 0xDA, 0xC0, 0xF3, 0xDB, 0xE7 ; Encrypted "h1s_f0r_"
    flag_part4 db 0xC6, 0xC2, 0xDB, 0xE4 ; Encrypted "m3}"

    key db 0xAC ; XOR key used for obfuscation

    ; Message to display
    msg db 'Enter input: ', 0
    msg_len equ $ - msg

section .bss
    input resb 100 ; Buffer for user input

section .text
    global _start

_start:
    ; Write prompt to stdout
    mov eax, 4          ; syscall number for sys_write
    mov ebx, 1          ; file descriptor 1 is stdout
    mov ecx, msg        ; pointer to the message
    mov edx, msg_len    ; length of the message
    int 0x80            ; call kernel

    ; Read user input
    mov eax, 3          ; syscall number for sys_read
    mov ebx, 0          ; file descriptor 0 is stdin
    mov ecx, input      ; pointer to the input buffer
    mov edx, 100        ; number of bytes to read
    int 0x80            ; call kernel

    ; Remove newline character from input if present
    mov byte [ecx + eax - 1], 0

    ; Decrypt the flag
    mov ecx, flag_part1
    mov edx, 8          ; Number of bytes to decrypt
    call decrypt

    mov ecx, flag_part2
    mov edx, 8
    call decrypt

    mov ecx, flag_part3
    mov edx, 8
    call decrypt

    mov ecx, flag_part4
    mov edx, 4
    call decrypt

    ; Output decrypted flag
    mov eax, 4
    mov ebx, 1
    mov ecx, flag_part1 ; Display flag part 1
    mov edx, 8          ; Length of flag part 1
    int 0x80

    mov ecx, flag_part2 ; Display flag part 2
    mov edx, 8          ; Length of flag part 2
    int 0x80

    mov ecx, flag_part3 ; Display flag part 3
    mov edx, 8          ; Length of flag part 3
    int 0x80

    mov ecx, flag_part4 ; Display flag part 4
    mov edx, 4          ; Length of flag part 4
    int 0x80

    ; Exit the program
    mov eax, 1          ; syscall number for sys_exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; call kernel

decrypt:
    ; Decrypt flag data using XOR
    xor ebx, ebx        ; Clear ebx (used as the pointer)
decrypt_loop:
    mov al, [ecx + ebx]
    xor al, [key]
    mov [ecx + ebx], al
    inc ebx
    dec edx
    jnz decrypt_loop
    ret

