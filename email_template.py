def mail_template_creation(receiver_name, date_1, date_2, document_link, client_name, client_contact, client_case_ov):
    return """
    <!--
* This email was built using Tabular.
* For more information, visit https://tabular.email
-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
<head>
<title></title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<!--[if !mso]><!-->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--<![endif]-->
<meta name="x-apple-disable-message-reformatting" content="" />
<meta content="target-densitydpi=device-dpi" name="viewport" />
<meta content="true" name="HandheldFriendly" />
<meta content="width=device-width" name="viewport" />
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
<style type="text/css">
table {
border-collapse: separate;
table-layout: fixed;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt
}
table td {
border-collapse: collapse
}
.ExternalClass {
width: 100%
}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
line-height: 100%
}
body, a, li, p, h1, h2, h3 {
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%;
}
html {
-webkit-text-size-adjust: none !important
}
body, #innerTable {
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale
}
#innerTable img+div {
display: none;
display: none !important
}
img {
Margin: 0;
padding: 0;
-ms-interpolation-mode: bicubic
}
h1, h2, h3, p, a {
line-height: 1;
overflow-wrap: normal;
white-space: normal;
word-break: break-word
}
a {
text-decoration: none
}
h1, h2, h3, p {
min-width: 100%!important;
width: 100%!important;
max-width: 100%!important;
display: inline-block!important;
border: 0;
padding: 0;
margin: 0
}
a[x-apple-data-detectors] {
color: inherit !important;
text-decoration: none !important;
font-size: inherit !important;
font-family: inherit !important;
font-weight: inherit !important;
line-height: inherit !important
}
a[href^="mailto"],
a[href^="tel"],
a[href^="sms"] {
color: inherit;
text-decoration: none
}
</style>
<style type="text/css">
@media (min-width: 481px) {
.hd { display: none!important }
}
</style>
<style type="text/css">
@media (max-width: 480px) {
.hm { display: none!important }
}
</style>
<style type="text/css">
[style*="Inter"] {font-family: 'Inter', BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif !important;} [style*="Inter Tight"] {font-family: 'Inter Tight', BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif !important;} [style*="Albert Sans"] {font-family: 'Albert Sans', BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif !important;}
@media only screen and (min-width: 481px) {.t6{width:520px!important}.t18{width:14.48517%!important}.t28{width:85.51483%!important;max-width:490px!important}.t38{max-width:453px!important}.t46{width:555px!important}.t54{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}.t56{max-width:840px!important}.t65,.t87{width:800px!important}.t102{width:510px!important}.t106{width:560px!important}.t118{width:21.22959%!important}.t126{width:78.77041%!important;max-width:820px!important}.t135{padding-left:10px!important;width:590px!important}.t140{padding-left:10px!important}.t145{padding-left:10px!important;width:590px!important}.t150{padding-left:10px!important}.t155{padding-left:10px!important;width:590px!important}.t160{padding-left:10px!important}.t165{width:570px!important}.t180{width:549px!important}.t184{width:800px!important}.t196{width:11.18421%!important}.t204{width:88.81579%!important;max-width:540px!important}.t213{width:600px!important}.t223{width:800px!important}.t235{width:11.18421%!important}.t243{width:88.81579%!important;max-width:540px!important}.t252{width:600px!important}.t262{width:800px!important}.t274{width:11.18421%!important}.t282{width:88.81579%!important;max-width:540px!important}.t291{width:600px!important}.t301{max-width:494px!important}.t302{padding-left:inherit!important;padding-right:inherit!important}.t304,.t306{border-radius:12px!important;overflow:hidden!important}.t310{width:800px!important}.t322{width:25%!important}.t332{width:75%!important;max-width:600px!important}.t340{width:800px!important}.t352{width:25%!important}.t362{width:75%!important;max-width:600px!important}.t370{width:800px!important}.t390{width:600px!important}.t403{padding:45px 50px!important}.t405{padding:45px 50px!important;width:500px!important}.t419{padding-bottom:10px!important;width:800px!important}.t424{padding-bottom:10px!important}.t479,.t489,.t500{width:600px!important}.t510,.t520,.t530,.t540,.t550,.t560{width:800px!important}}
</style>
<style type="text/css" media="screen and (min-width:481px)">.moz-text-html .t6{width:520px!important}.moz-text-html .t18{width:14.48517%!important}.moz-text-html .t28{width:85.51483%!important;max-width:490px!important}.moz-text-html .t38{max-width:453px!important}.moz-text-html .t46{width:555px!important}.moz-text-html .t54{mso-line-height-alt:0px!important;line-height:0!important;display:none!important}.moz-text-html .t56{max-width:840px!important}.moz-text-html .t65,.moz-text-html .t87{width:800px!important}.moz-text-html .t102{width:510px!important}.moz-text-html .t106{width:560px!important}.moz-text-html .t118{width:21.22959%!important}.moz-text-html .t126{width:78.77041%!important;max-width:820px!important}.moz-text-html .t135{padding-left:10px!important;width:590px!important}.moz-text-html .t140{padding-left:10px!important}.moz-text-html .t145{padding-left:10px!important;width:590px!important}.moz-text-html .t150{padding-left:10px!important}.moz-text-html .t155{padding-left:10px!important;width:590px!important}.moz-text-html .t160{padding-left:10px!important}.moz-text-html .t165{width:570px!important}.moz-text-html .t180{width:549px!important}.moz-text-html .t184{width:800px!important}.moz-text-html .t196{width:11.18421%!important}.moz-text-html .t204{width:88.81579%!important;max-width:540px!important}.moz-text-html .t213{width:600px!important}.moz-text-html .t223{width:800px!important}.moz-text-html .t235{width:11.18421%!important}.moz-text-html .t243{width:88.81579%!important;max-width:540px!important}.moz-text-html .t252{width:600px!important}.moz-text-html .t262{width:800px!important}.moz-text-html .t274{width:11.18421%!important}.moz-text-html .t282{width:88.81579%!important;max-width:540px!important}.moz-text-html .t291{width:600px!important}.moz-text-html .t301{max-width:494px!important}.moz-text-html .t302{padding-left:inherit!important;padding-right:inherit!important}.moz-text-html .t304,.moz-text-html .t306{border-radius:12px!important;overflow:hidden!important}.moz-text-html .t310{width:800px!important}.moz-text-html .t322{width:25%!important}.moz-text-html .t332{width:75%!important;max-width:600px!important}.moz-text-html .t340{width:800px!important}.moz-text-html .t352{width:25%!important}.moz-text-html .t362{width:75%!important;max-width:600px!important}.moz-text-html .t370{width:800px!important}.moz-text-html .t390{width:600px!important}.moz-text-html .t403{padding:45px 50px!important}.moz-text-html .t405{padding:45px 50px!important;width:500px!important}.moz-text-html .t419{padding-bottom:10px!important;width:800px!important}.moz-text-html .t424{padding-bottom:10px!important}.moz-text-html .t479,.moz-text-html .t489,.moz-text-html .t500{width:600px!important}.moz-text-html .t510,.moz-text-html .t520,.moz-text-html .t530,.moz-text-html .t540,.moz-text-html .t550,.moz-text-html .t560{width:800px!important}</style>
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&amp;family=Albert+Sans:wght@500;700&amp;family=Inter:wght@400&amp;display=swap" rel="stylesheet" type="text/css" />
<!--<![endif]-->
<!--[if mso]>
<style type="text/css">
td.t6{width:600px !important}div.t18{width:14.48517% !important}td.t26{width:490px !important}div.t28{width:85.51483% !important;max-width:490px !important}td.t36{width:453px !important}div.t38{max-width:453px !important}td.t46{width:595px !important}div.t54{mso-line-height-alt:0px !important;line-height:0 !important;display:none !important}div.t56{max-width:840px !important}td.t61,td.t65,td.t87{width:800px !important}td.t102{width:590px !important}td.t106{width:600px !important}div.t118{width:21.22959% !important}div.t126{width:78.77041% !important;max-width:820px !important}td.t131{width:800px !important}td.t135{padding-left:10px !important;width:600px !important}td.t140{padding-left:10px !important}td.t145{padding-left:10px !important;width:600px !important}td.t150{padding-left:10px !important}td.t155{padding-left:10px !important;width:600px !important}td.t160{padding-left:10px !important}td.t165{width:600px !important}td.t180{width:589px !important}td.t184{width:800px !important}div.t196{width:11.18421% !important}div.t204{width:88.81579% !important;max-width:540px !important}td.t209{width:500px !important}td.t213{width:600px !important}td.t223{width:800px !important}div.t235{width:11.18421% !important}div.t243{width:88.81579% !important;max-width:540px !important}td.t248{width:500px !important}td.t252{width:600px !important}td.t262{width:800px !important}div.t274{width:11.18421% !important}div.t282{width:88.81579% !important;max-width:540px !important}td.t287{width:500px !important}td.t291{width:600px !important}div.t301{max-width:494px !important}div.t302{padding-left:inherit !important;padding-right:inherit !important}td.t304{border-radius:12px !important;overflow:hidden !important}td.t306{border-radius:12px !important;overflow:hidden !important;width:494px !important}td.t310{width:800px !important}div.t322{width:25% !important}td.t330{width:600px !important}div.t332{width:75% !important;max-width:600px !important}td.t340{width:800px !important}div.t352{width:25% !important}td.t360{width:600px !important}div.t362{width:75% !important;max-width:600px !important}td.t370{width:800px !important}td.t390{width:600px !important}td.t403{padding:45px 50px !important}td.t405{padding:45px 50px !important;width:600px !important}td.t419{padding-bottom:10px !important;width:800px !important}td.t424{padding-bottom:10px !important}td.t479,td.t489,td.t500{width:600px !important}td.t510,td.t520,td.t530,td.t540,td.t550,td.t560{width:800px !important}
</style>
<![endif]-->
<!--[if mso]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body class="t0" style="min-width:100%;Margin:0px;padding:0px;background-color:#ffffff;"><div class="t1" style="background-color:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t2" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#ffffff;" valign="top" align="center">
<!--[if mso]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
<v:fill color="#ffffff"/>
</v:background>
<![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td><div class="t3" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t5" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t6" style="background-color:#7367FF;overflow:hidden;width:400px;padding:10px 40px 10px 40px;border-radius:20px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t6" style="background-color:#7367FF;overflow:hidden;width:480px;padding:10px 40px 10px 40px;border-radius:20px 20px 20px 20px;"><![endif]-->
<div class="t12" style="display:inline-table;width:100%;text-align:center;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="middle" width="520"><tr><td width="75.32286" valign="middle"><![endif]-->
<div class="t18" style="display:inline-table;text-align:initial;vertical-align:inherit;width:14.74245%;max-width:83px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t20"><tr>
<td class="t21" style="overflow:hidden;border-radius:20px 20px 20px 20px;"><div style="font-size:0px;"><img class="t22" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="75.32286212914485" height="75.3125" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/03952486-b030-47d2-a57f-4c8c3ae3d1ec.png"/></div></td>
</tr></table>
</div>
<!--[if mso]>
</td><td width="444.67714" valign="middle"><![endif]-->
<div class="t28" style="display:inline-table;text-align:initial;vertical-align:inherit;width:85.25755%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t30"><tr>
<td class="t31"><div class="t32" style="display:inline-table;width:100%;text-align:right;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="right" valign="middle" width="444.67714"><tr><td width="444.67714" valign="middle"><![endif]-->
<div class="t38" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:346px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t40"><tr>
<td class="t41" style="padding:0 0 0 45px;"><p class="t42" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:30px;font-weight:600;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;direction:ltr;color:#FFFFFF;text-align:right;mso-line-height-rule:exactly;mso-text-raise:2px;">New Mandate Documents</p></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t4" style="mso-line-height-rule:exactly;mso-line-height-alt:19px;line-height:19px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t45" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t46" style="background-color:#FAFAFA;overflow:hidden;width:440px;padding:40px 20px 40px 20px;border-radius:20px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t46" style="background-color:#FAFAFA;overflow:hidden;width:480px;padding:40px 20px 40px 20px;border-radius:20px 20px 20px 20px;"><![endif]-->
<div class="t52" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="555"><tr><td class="t55" style="width:20px;" width="20"></td><td width="515" valign="top"><![endif]-->
<div class="t56" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:520px;"><div class="t57" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t58"><tr>
<td class="t59"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t64" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t65" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t65" style="width:480px;"><![endif]-->
<h1 class="t71" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:800;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;direction:ltr;color:#222222;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">Hi """ + receiver_name+ """,</h1></td>
</tr></table>
</td></tr><tr><td><div class="t63" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t529" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t530" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t530" style="width:480px;"><![endif]-->
<p class="t536" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">A new mandate has created an inquiry via your website! The needed documents have been created and you are able to find them attached in this mail ✉️!</p></td>
</tr></table>
</td></tr><tr><td><div class="t528" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t539" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t540" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t540" style="width:480px;"><![endif]-->
<p class="t546" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">According to your calendar the following dates would be available for a first meeting session with the new client:</p></td>
</tr></table>
</td></tr><tr><td><div class="t538" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t559" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t560" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t560" style="width:480px;"><![endif]-->
<p class="t566" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">- """ + date_1 + """</p></td>
</tr></table>
</td></tr><tr><td><div class="t558" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t549" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t550" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t550" style="width:480px;"><![endif]-->
<p class="t556" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">- """ + date_2 + """</p></td>
</tr></table>
</td></tr><tr><td><div class="t548" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t509" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t510" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t510" style="width:480px;"><![endif]-->
<p class="t516" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">If you have any additional questions or missing information slots, feel free to contact us anytime!</p></td>
</tr></table>
</td></tr><tr><td><div class="t508" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t519" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t520" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t520" style="width:480px;"><![endif]-->
<p class="t526" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Kind regards,</p></td>
</tr></table>
</td></tr><tr><td><div class="t518" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t86" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t87" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t87" style="width:480px;"><![endif]-->
<p class="t93" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:26px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Your favourite RightRouteAI Bot 🤖🧑🏻‍⚖️</p></td>
</tr></table>
</td></tr><tr><td><div class="t85" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t74" role="presentation" cellpadding="0" cellspacing="0" align="left"><tr>
<!--[if !mso]><!--><td class="t75" style="background-color:#7367FF;overflow:hidden;width:100px;text-align:center;line-height:36px;mso-line-height-rule:exactly;mso-text-raise:7px;border-radius:8px 8px 8px 8px;">
<!--<![endif]-->
<!--[if mso]><td class="t75" style="background-color:#7367FF;overflow:hidden;width:100px;text-align:center;line-height:36px;mso-line-height-rule:exactly;mso-text-raise:7px;border-radius:8px 8px 8px 8px;"><![endif]-->
<a class="t81" href="https://tech-challenge-23-landing.bubbleapps.io/version-test/" style="display:block;margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:36px;font-weight:700;font-style:normal;font-size:14px;text-decoration:none;direction:ltr;color:#FFFFFF;text-align:center;mso-line-height-rule:exactly;mso-text-raise:7px;" target="_blank">Questions?</a></td>
</tr></table>
</td></tr></table></td>
</tr></table>
<!--[if !mso]><!--><div class="t54" style="mso-line-height-rule:exactly;mso-line-height-alt:40px;line-height:40px;font-size:1px;display:block;">&nbsp;</div>
<!--<![endif]-->
</div></div>
<!--[if mso]>
</td><td class="t55" style="width:20px;" width="20"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t44" style="mso-line-height-rule:exactly;mso-line-height-alt:19px;line-height:19px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t101" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t102" style="background-color:#FAFAFA;overflow:hidden;width:400px;padding:19px 40px 19px 40px;border-radius:20px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t102" style="background-color:#FAFAFA;overflow:hidden;width:480px;padding:19px 40px 19px 40px;border-radius:20px 20px 20px 20px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t105" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t106" style="background-color:#F0F0F0;overflow:hidden;width:440px;padding:20px 20px 20px 20px;border-radius:20px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t106" style="background-color:#F0F0F0;overflow:hidden;width:480px;padding:20px 20px 20px 20px;border-radius:20px 20px 20px 20px;"><![endif]-->
<div class="t112" style="display:inline-table;width:100%;text-align:left;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="middle" width="470"><tr><td class="t117" style="width:10px;" width="10"></td><td width="86.34366" valign="middle"><![endif]-->
<div class="t118" style="display:inline-table;text-align:initial;vertical-align:inherit;width:30.65187%;max-width:221px;"><div class="t119" style="padding:0 10px 0 10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t120"><tr>
<td class="t121"><a href="*INSERT URL FOR PDF HERE*" style="font-size:0px;" target="_blank"><img class="t122" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="86.34365634365635" height="79.765625" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/6cc8d9c0-b426-4c10-a690-b4a61eb8be53.png"/></a></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t117" style="width:10px;" width="10"></td><td class="t125" style="width:10px;" width="10"></td><td width="343.65634" valign="middle"><![endif]-->
<div class="t126" style="display:inline-table;text-align:initial;vertical-align:inherit;width:69.34813%;max-width:500px;"><div class="t127" style="padding:0 10px 0 10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t128"><tr>
<td class="t129"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t134" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t135" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t135" style="width:480px;"><![endif]-->
<h1 class="t141" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:700;font-style:normal;font-size:14px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">new_mandate_form_""" + client_name + """</h1></td>
</tr></table>
</td></tr><tr><td><div class="t133" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t144" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t145" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t145" style="width:480px;"><![endif]-->
<h1 class="t151" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">Filled out document with new mandate and case information for a new mandate file.</h1></td>
</tr></table>
</td></tr><tr><td><div class="t152" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t154" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t155" style="border-top:1px solid #CCCCCC;width:480px;padding:15px 0 0 0;">
<!--<![endif]-->
<!--[if mso]><td class="t155" style="border-top:1px solid #CCCCCC;width:480px;padding:15px 0 0 0;"><![endif]-->
<h1 class="t161" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:16px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;direction:ltr;color:#1A1A1A;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">Number of documents: 1</h1></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t125" style="width:10px;" width="10"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t104" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t164" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t165" style="background-color:#F0F0F0;overflow:hidden;width:450px;padding:10px 15px 10px 15px;border-radius:20px 20px 20px 20px;">
<!--<![endif]-->
<!--[if mso]><td class="t165" style="background-color:#F0F0F0;overflow:hidden;width:480px;padding:10px 15px 10px 15px;border-radius:20px 20px 20px 20px;"><![endif]-->
<div class="t171" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="480"><tr><td width="480" valign="top"><![endif]-->
<div class="t301" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:480px;"><div class="t298" style="mso-line-height-rule:exactly;mso-line-height-alt:5px;line-height:5px;font-size:1px;display:block;">&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t303"><tr>
<td class="t304" style="background-color:#FFFFFF;padding:20px 40px 20px 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t309" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t310" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t310" style="width:480px;"><![endif]-->
<div class="t316" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="400"><tr><td width="100" valign="top"><![endif]-->
<div class="t322" style="display:inline-table;text-align:initial;vertical-align:inherit;width:29.41176%;max-width:200px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t324"><tr>
<td class="t325"><p class="t326" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:600;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">Name:</p></td>
</tr></table>
</div>
<!--[if mso]>
</td><td width="300" valign="top"><![endif]-->
<div class="t332" style="display:inline-table;text-align:initial;vertical-align:inherit;width:70.58824%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t334"><tr>
<td class="t335"><p class="t336" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#787878;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">""" + client_name + """</p></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t337" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t339" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t340" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t340" style="width:480px;"><![endif]-->
<div class="t346" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="400"><tr><td width="100" valign="top"><![endif]-->
<div class="t352" style="display:inline-table;text-align:initial;vertical-align:inherit;width:29.41176%;max-width:200px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t354"><tr>
<td class="t355"><p class="t356" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:600;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">Contact:</p></td>
</tr></table>
</div>
<!--[if mso]>
</td><td width="300" valign="top"><![endif]-->
<div class="t362" style="display:inline-table;text-align:initial;vertical-align:inherit;width:70.58824%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t364"><tr>
<td class="t365"><p class="t366" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#787878;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">""" + client_contact + """</p></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t367" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t369" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t370" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t370" style="width:480px;"><![endif]-->
<div class="t376" style="display:inline-table;width:100%;text-align:left;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top" width="200"><tr><td width="200" valign="top"><![endif]-->
<div class="t382" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:200px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t384"><tr>
<td class="t385"><p class="t386" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:600;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">Case Overview</p></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t387" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t389" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t390" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t390" style="width:480px;"><![endif]-->
<p class="t396" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:500;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#787878;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">""" + client_case_ov + """</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
<div class="t299" style="mso-line-height-rule:exactly;mso-line-height-alt:5px;line-height:5px;font-size:1px;display:block;">&nbsp;</div></div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr><tr><td><div class="t95" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t179" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t180" style="background-color:#FFFFFF;overflow:hidden;width:440px;padding:40px 20px 40px 20px;border-radius:8px 8px 8px 8px;">
<!--<![endif]-->
<!--[if mso]><td class="t180" style="background-color:#FFFFFF;overflow:hidden;width:480px;padding:40px 20px 40px 20px;border-radius:8px 8px 8px 8px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t183" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t184" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t184" style="width:480px;"><![endif]-->
<div class="t190" style="display:inline-table;width:100%;text-align:left;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="middle" width="549"><tr><td class="t195" style="width:20px;" width="20"></td><td width="24.87121" valign="middle"><![endif]-->
<div class="t196" style="display:inline-table;text-align:initial;vertical-align:inherit;width:11.56463%;max-width:68px;"><div class="t197" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t198"><tr>
<td class="t199"><div style="font-size:0px;"><img class="t200" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="24.87121212121212" height="21.390625" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/0be22f60-4628-4776-ac0d-8f554e792b18.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t195" style="width:20px;" width="20"></td><td class="t203" style="width:20px;" width="20"></td><td width="444.12879" valign="middle"><![endif]-->
<div class="t204" style="display:inline-table;text-align:initial;vertical-align:inherit;width:88.43537%;max-width:520px;"><div class="t205" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t206"><tr>
<td class="t207"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t212" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t213" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t213" style="width:480px;"><![endif]-->
<p class="t219" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:800;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;direction:ltr;color:#222222;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">24/7 customer support, we&#39;ll be here for you.</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t203" style="width:20px;" width="20"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t220" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t222" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t223" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t223" style="width:480px;"><![endif]-->
<div class="t229" style="display:inline-table;width:100%;text-align:left;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="middle" width="549"><tr><td class="t234" style="width:20px;" width="20"></td><td width="24.87121" valign="middle"><![endif]-->
<div class="t235" style="display:inline-table;text-align:initial;vertical-align:inherit;width:11.56463%;max-width:68px;"><div class="t236" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t237"><tr>
<td class="t238"><div style="font-size:0px;"><img class="t239" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="24.87121212121212" height="21.390625" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/0be22f60-4628-4776-ac0d-8f554e792b18.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t234" style="width:20px;" width="20"></td><td class="t242" style="width:20px;" width="20"></td><td width="444.12879" valign="middle"><![endif]-->
<div class="t243" style="display:inline-table;text-align:initial;vertical-align:inherit;width:88.43537%;max-width:520px;"><div class="t244" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t245"><tr>
<td class="t246"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t251" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t252" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t252" style="width:480px;"><![endif]-->
<p class="t258" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:800;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;direction:ltr;color:#222222;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">Automated Document Creation</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t242" style="width:20px;" width="20"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t259" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t261" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t262" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t262" style="width:480px;"><![endif]-->
<div class="t268" style="display:inline-table;width:100%;text-align:left;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="left" valign="middle" width="549"><tr><td class="t273" style="width:20px;" width="20"></td><td width="24.87121" valign="middle"><![endif]-->
<div class="t274" style="display:inline-table;text-align:initial;vertical-align:inherit;width:11.56463%;max-width:68px;"><div class="t275" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t276"><tr>
<td class="t277"><div style="font-size:0px;"><img class="t278" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="24.87121212121212" height="21.390625" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/0be22f60-4628-4776-ac0d-8f554e792b18.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t273" style="width:20px;" width="20"></td><td class="t281" style="width:20px;" width="20"></td><td width="444.12879" valign="middle"><![endif]-->
<div class="t282" style="display:inline-table;text-align:initial;vertical-align:inherit;width:88.43537%;max-width:520px;"><div class="t283" style="padding:0 20px 0 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t284"><tr>
<td class="t285"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t290" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t291" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t291" style="width:480px;"><![endif]-->
<p class="t297" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter Tight';line-height:22px;font-weight:800;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;direction:ltr;color:#222222;text-align:left;mso-line-height-rule:exactly;mso-text-raise:1px;">Validated Data Collection</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t281" style="width:20px;" width="20"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr><tr><td><div class="t173" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t404" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t405" style="background-color:#FFFFFF;width:420px;padding:40px 30px 40px 30px;">
<!--<![endif]-->
<!--[if mso]><td class="t405" style="background-color:#FFFFFF;width:480px;padding:40px 30px 40px 30px;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t408" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t409" style="width:195px;">
<!--<![endif]-->
<!--[if mso]><td class="t409" style="width:195px;"><![endif]-->
<div style="font-size:0px;"><img class="t415" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="195" height="67.484375" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/377235b6-249e-4af1-a609-caab0cd8ddab.png"/></div></td>
</tr></table>
</td></tr><tr><td><div class="t416" style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t418" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t419" style="width:480px;padding:10px 0 36px 0;">
<!--<![endif]-->
<!--[if mso]><td class="t419" style="width:480px;padding:10px 0 36px 0;"><![endif]-->
<div class="t425" style="display:inline-table;width:100%;text-align:center;vertical-align:middle;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="middle" width="320"><tr><td class="t430" style="width:17px;" width="17"></td><td width="29" valign="middle"><![endif]-->
<div class="t431" style="display:inline-table;text-align:initial;vertical-align:inherit;width:19.6875%;max-width:63px;"><div class="t432" style="padding:0 17px 0 17px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t433"><tr>
<td class="t434"><div style="font-size:0px;"><img class="t435" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="29" height="29" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/90ff3c53-3cc5-4ec6-88d1-5c98259ede75.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t430" style="width:17px;" width="17"></td><td class="t440" style="width:17px;" width="17"></td><td width="29" valign="middle"><![endif]-->
<div class="t441" style="display:inline-table;text-align:initial;vertical-align:inherit;width:19.6875%;max-width:63px;"><div class="t442" style="padding:0 17px 0 17px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t443"><tr>
<td class="t444"><div style="font-size:0px;"><img class="t445" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="29" height="28.34375" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/32ac7e8e-de26-4126-916e-6565ab0fc12f.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t440" style="width:17px;" width="17"></td><td class="t450" style="width:17px;" width="17"></td><td width="29" valign="middle"><![endif]-->
<div class="t451" style="display:inline-table;text-align:initial;vertical-align:inherit;width:19.6875%;max-width:63px;"><div class="t452" style="padding:0 17px 0 17px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t453"><tr>
<td class="t454"><div style="font-size:0px;"><img class="t455" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="29" height="34.265625" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/e97b53b5-215b-4896-bfdc-557915355675.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t450" style="width:17px;" width="17"></td><td class="t460" style="width:17px;" width="17"></td><td width="34" valign="middle"><![endif]-->
<div class="t461" style="display:inline-table;text-align:initial;vertical-align:inherit;width:21.25%;max-width:68px;"><div class="t462" style="padding:0 17px 0 17px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t463"><tr>
<td class="t464"><div style="font-size:0px;"><img class="t465" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="34" height="23.734375" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/1dc80ec4-388b-476f-9db9-4ff8d40f19e8.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t460" style="width:17px;" width="17"></td><td class="t470" style="width:17px;" width="17"></td><td width="29" valign="middle"><![endif]-->
<div class="t471" style="display:inline-table;text-align:initial;vertical-align:inherit;width:19.6875%;max-width:63px;"><div class="t472" style="padding:0 17px 0 17px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t473"><tr>
<td class="t474"><div style="font-size:0px;"><img class="t475" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="29" height="23.1875" alt="" src="https://uploads.tabular.email/e/701959f8-8fbf-4414-83ea-85389d622dd5/91e9d190-2061-444d-ad80-a8257b15cd75.png"/></div></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t470" style="width:17px;" width="17"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr><tr><td><div class="t476" style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t478" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t479" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t479" style="width:480px;"><![endif]-->
<p class="t485" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter';line-height:21px;font-weight:400;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px;">RightRoute Street 22, Munich Germany</p></td>
</tr></table>
</td></tr><tr><td><div class="t486" style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t488" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t489" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t489" style="width:480px;"><![endif]-->
<p class="t495" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Albert Sans';line-height:22px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#888888;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;"><a class="t496" href="https://tabular.email" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter';line-height:21px;font-weight:400;font-style:normal;font-size:14px;text-decoration:underline;direction:ltr;color:#000000;mso-line-height-rule:exactly;mso-text-raise:2px;" target="_blank">Contact</a></p></td>
</tr></table>
</td></tr><tr><td><div class="t497" style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t499" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t500" style="width:480px;">
<!--<![endif]-->
<!--[if mso]><td class="t500" style="width:480px;"><![endif]-->
<p class="t506" style="margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Inter';line-height:21px;font-weight:400;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">Copyright © 2024 All rights reserved.</p></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr></table></td></tr></table></div></body>
</html>

"""
