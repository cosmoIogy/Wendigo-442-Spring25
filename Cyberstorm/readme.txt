PROGRAM 1: ( binary to text convertion )

	python3 binary_decoder.py < *file*

PROGRAM 2: ( vigenere cipher )
	
	- Decrypt:
	
		python3 vigenere_cipher.py -d *key*
	
		- Then type / copy and paste your cipher text

	- Encrypt:

		python3 vigenere_cipher.py -e *key*

		- Then type / copy and paste your plain text

PROGRAM 3: ( FTP (storage) covert channel )

	- Open the file "ftp_covert_channel.py" and edit the lines containing
		- username
		- password
		- port
		- host
		- filepath
		- METHOD

	- TO RUN:
		python3 ftp_covert_channel.py


PROGRAM 4: ( chat (timing) covert channel )

	- Open the file "chat_client.py" and edit the lines containing
		- ip
		- port
		- threshold
			- For the threshold, you may have to experiment with the debug turned on to get the correct threshold
	
	- TO RUN:
		python3 chat_client.py

PROGRAM 5: ( timelock )

	- TO RUN:
		echo "2000 00 00 00 00 00" | python3 timelock.py

	Where "2000 00 00 00 00 00" is the epoch time, usually found in a hint.
	You can manually change the epoch time by changing the DEBUG to true, and update the "cur2" variable

PROGRAM 6: ( xor )

	Create a file named "key" and insert the key into the file
	
	- TO RUN:	
		- DECRYPT:
			python3 xor.py < *ciphertext*

		- ENCRYPT:
			python3 xor.py < *plaintext* > *ciphertext*

PROGRAM 7: ( steg )

	Usage:
		python steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
			-s store
			-r retrieve
			-b bit mode
			-B byte mode
			-o<val> set offset to <val> (default is 0)
			-i<val> set interval to <val> (default is 1)
			-w<val> set wrapper file to <val>
			-h<val> set hidden file to <val>

	Example:
		- RETRIEVE bits:
			python3 steg.py -r -b -o32 -i64 -wnew.jpg > extracted.jpg

		- STORE bytes:
			python3 steg.py -s -B -o64 -i32 -wimage.jpg -hsecret.jpg > new.jpg
