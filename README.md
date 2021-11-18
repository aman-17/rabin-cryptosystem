# RABIN_CRYPTOSYSTEM

The  modular  square  root  problem  has  a  special  property  of  the  having  com-putational equivalent to a well-known hard mathematical problem namely integerfactorization problem.  The Rabin scheme used in public-key cryptosystem is hererevisited with a focus limited to a few specific open issues.  In particular, messagedecryption requires one out of four roots of a quadratic equation in a residue ringto be chosen, and a longstanding problem is to identify unambiguously and deter-ministically the encrypted message at the decryption side by adding the minimumnumber of extra bits to the cipher-text.  The proposed Rabin-p Key EncapsulationMechanism is built upon the said problem as its source of security, aiming for effi-cient and practical modular square root-based cryptosystem of which accompaniedwith the following properties:
* Improves  the  performance  without  plaintext  padding  mechanisms  or  sendingextra bits during encryption and decryption processes.
* The plaintext is uniquely decrypted without decryption failure.
* Improve decryption efficiency by using only one modular exponentiation.
* A decryption key using a single prime number.
* It has sufficient large plaintext space.

Rabin Cryptosystem is an public-key cryptosystem invented by Michael Rabin. It usesasymmetric key encryption for communicating between two parties and encrypting themessage.The Rabin encryption scheme is one of an existing workable asymmetric cryptosystemthat comes with nice cryptographic properties.  For instance, it has low-cost encryptionof which the Rabin encryption is relatively fast to encrypt compared to the widely com-mercialized RSA cryptosystem, and it has been proven to be as difficult as the integerfactorization problem.  On the other hand,  the decryption of Rabin’s scheme producesfour possible answers, which only one is correct.  This four-to-one decryption setting ofthe Rabin decryption could lead to a decryption failure scenario since no indicator forselecting the correct plaintext is given. We revisit the Rabin cryptosystem and then aspire to furnish a new design aiming forefficient, secure and practical Rabin-like cryptosystem.

My primary programming language is Python, so I will make use of the Rabin Algorithmfor making an encryption and decryption program in Python.  We are also going to usefew python libraries to make code easy as we have large mathematical operations.  Thereare  three  inputs  for  Rabin  512  encryption  and  decryption  1  output  for  each  of  themrespectively.

## Read the Rabin_crypto_system.pdf.
