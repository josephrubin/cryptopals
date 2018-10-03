#!/usr/bin/env python3
import user
import pad


def _main():
    # Oracle looks like:
    # email=foo@bar.com&uid=10&role=user

    # Plan: get the role=user part to be at the start of a block,
    #       and cut it out. Then paste in the encryption for
    #       role=admin. It is that easy.
    uid_len = len('&uid=10&')
    role_prefix_len = len('role=')
    email_prefix_len = len('email=')

    # We need to block align the 'user' so we can cut it out.
    total_len = email_prefix_len + role_prefix_len + uid_len
    desired_email_len = (((total_len // 16) + 1) * 16) - total_len
    email = 'a' * desired_email_len
    cipher = user.oracle(email) 
    
    print('Current user:', user.unoracle(cipher))

    # Cut out the 'user'.
    cipher = cipher[:-16]

    # To put in an admin, we must figure out how it is encrypted.
    # We do this by aligning it in the email as a padded block
    # and then select it from the ciphertext.
    desired_real_email_len = 16 - email_prefix_len
    real_email = 'a' * desired_real_email_len
    email = real_email + pad.pkcs7(b'admin', 16).decode('ascii')
    cipher_2 = user.oracle(email)

    # Now the second block should be the encrypted form of the
    # well-padded 'admin' text.
    admin_cipher = cipher_2[16:32]

    # Now paste that on to our old user account.
    cipher += admin_cipher

    print('Newly adminified:', user.unoracle(cipher))


if __name__ == '__main__':
    _main()
