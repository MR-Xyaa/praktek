<?php


$email = $_REQUEST['email'] ;

require("C:/inetpub/mysite.com/PHPMailer/PHPMailerAutoload.php");

$mail = new PHPMailer();

// set mailer to use SMTP
$mail->IsSMTP();

$mail->Host = "smtp.comcast.net"; // specify main and backup server
$mail->SMTPAuth = true; // turn on SMTP authentication
$mail->Username = "myusername@comcast.net"; // SMTP username
$mail->Password = "*******"; // SMTP password
$mail->SMTPSecure = 'ssl';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 25;                                    


$mail->From = $email;

// below we want to set the email address we will be sending our email to.
$mail->AddAddress("myemail@gmail.com", "Guestlist");

// set word wrap to 50 characters
$mail->WordWrap = 50;
// set email format to HTML
$mail->IsHTML(true);

$mail->Subject = "A new member wishes to be added";

$message = $_REQUEST['message'] ;
$mail->Body = $email;
$mail->AltBody = $email;

if(!$mail->Send())
{
echo "Message could not be sent. <p>";
echo "Mailer Error: " . $mail->ErrorInfo;
exit;
}

echo "Message has been sent";

$mail2 = new PHPMailer();

// set mailer to use SMTP
$mail2->IsSMTP();

$mail2->Host = "smtp.comcast.net"; // specify main and backup server
$mail2->SMTPAuth = true; // turn on SMTP authentication
$mail2->Username = "myusername@comcast.net"; // SMTP username
$mail2->Password = "*******"; // SMTP password
$mail2->SMTPSecure = 'ssl';                            // Enable TLS encryption, `ssl` also accepted
$mail2->Port = 25;                                    


$mail2->From = $email;

// below we want to set the email address we will be sending our email to.
$mail2->AddAddress("$email");

// set word wrap to 50 characters
$mail2->WordWrap = 50;
// set email format to HTML
$mail2->IsHTML(true);

$mail2->Subject = "Thank you for joining";

$message = "Please stay tune for updates" ;

$message = $_REQUEST['message'] ;
$mail2->Body = $message;
$mail2->AltBody = $message;

if(!$mail2->Send())
{
echo "Message could not be sent. <p>";
echo "Mailer Error: " . $mail2->ErrorInfo;
exit;
}

echo "Message has been sent";
?>
Update: 1 Ok, I figured out how to send auto-respond emails to users. However, now the users are receiving messages with their own email address and the name Root user

So what can I do to fix this problem so that users see my email address when they recevie auto-responses, and how can I make sure it says my name instead of root user?

php
email
phpmyadmin
phpmailer
contact-form
Share
Improve this question
Follow
edited Jul 1, 2015 at 0:16
asked Jun 30, 2015 at 22:55
user avatar
ChosenJuan
84122 gold badges2121 silver badges5353 bronze badges
insert email address in to db-> send email to user. its not clear what you are stuck with – 
user557846
 Jun 30, 2015 at 22:58
just create some new variables (e.g. $usermail or something like that) and a another message variable with the thank you message, and the email variable, and then run the 
