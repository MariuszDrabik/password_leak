<h1>Password validator</h1>

<p>Program to validate passwords. When password is validated successfully, Leaked module
is used to verified that SH1 hash of password are leaked. If not, passwords positively verified are saved to file.</p>

<p>Password are read from file passwords.txt -> Verification -> saved in to files:</p>
<ul>
    <li>weak_passwd.txt -> info what is wrong with password</li>
    <li>good_passwd.txt -> info which passwords are safe</li>
</ul>
<p>Module PasswdValidator can be used separately with You program.</p>
