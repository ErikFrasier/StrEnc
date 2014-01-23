StrEnc
======

Python based string encoding tool<br>
<br>
StrEnc is an extremely simple script that simply encodes a user supplied string using various common methods such as URL, double URL, String.fromCharCode, Base 64, Ascii Hex, and Hex.<br>
<br>
StrEnc v0.1<br>
<br>
-? usage<br>
-h help/usage<br>
-s "\<string to be encoded\>" (note: quotes required)<br>
<br>
Example:<br>
\$ ./StrEnc.py -s "\<script>alert(1)\</script>"<br>
\=================================================================================================================<br>
Input string to be encoded: 	\<script>alert(1)\</script><br>
\=================================================================================================================<br>
URL encoding: 			%3Cscript%3Ealert%281%29%3C%2Fscript%3E<br>
Double URL encoding:	 	%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E<br>
String.fromCharCode: 		String.fromCharCode(60,115,99,114,105,112,116,62,97,108,101,114,116,40,49,41,60,47,115,99,114,105,112,116,62)<br>
Base64 encoding: 		PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==<br>
Ascii Hex encoding: 		3c7363726970743e616c6572742831293c2f7363726970743e<br>
Hex encoding: 			3c:73:63:72:69:70:74:3e:61:6c:65:72:74:28:31:29:3c:2f:73:63:72:69:70:74:3e<br>
<br>

Questions? Erik.Frasier@knowledgecg.com
