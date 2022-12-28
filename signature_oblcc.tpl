{% if data %}
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width">
<title>Oblivion</title>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:100' rel='stylesheet' type='text/css'>
</head>

<body>
	<table width="300" border="0" cellspacing="0" cellpadding="5" style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-family: 'Trebuchet MS', Arial, sans-serif; font-size: 11pt; line-height: 19px;" summary="Oblivion">
    <tbody>
        <tr>
            <td style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; margin: 0px;"><img
                    src="https://assets.oblcc.com/oblivion-logo.png" width="250" height="60" alt="Oblivion"></td>
        </tr>
        <tr>
            <td
                style="margin: 0px; font-size: 11pt; color: rgb(0, 128, 200); padding: 10px 0px; border-top-width: 1px; border-top-style: solid; border-top-color: rgb(243, 243, 243);">
                <b>{{ data["full_name"] }}</b>&nbsp;<a href="{{ data["linkedin_url"] }}" target="_blank"><img
                        src="https://assets.oblcc.com/ln.png" width="11" alt="LinkedIn"></a><br>{{ data["job_role"] }}</td>
        </tr>
        <tr>
            <td
                style="margin: 0px; font-size: 10pt; padding: 10px 0px; border-top-width: 1px; border-top-style: solid; border-top-color: rgb(243, 243, 243);">
                <a href="tel:{{ data["phone"] | replace(" ", "") }}" target="_blank" style="color: rgb(0, 0, 0); border-bottom-width: 0px;">{{ data["phone"] }}</a><br><a href="tel:+31202103750" target="_blank"
                    style="color: rgb(0, 0, 0); border-bottom-width: 0px;">+31 20 210 37 50</a><br><a
                    href="https://oblcc.com/" target="_blank"
                    style="color: rgb(0, 0, 0); border-bottom-width: 0px;">https://www.oblcc.com</a><br>Amsterdam&nbsp;<span
                    style="color: rgb(0, 128, 200);">|</span>&nbsp;Apeldoorn&nbsp;<span
                    style="color: rgb(0, 128, 200);">|</span>&nbsp;Bonn&nbsp;<span
                    style="color: rgb(0, 128, 200);">|</span>&nbsp;Aarhus</td>
        </tr>
        <tr>
            <td
                style="margin: 0px; font-size: 9pt; padding: 10px 0px; border-top-width: 1px; border-top-style: solid; border-top-color: rgb(243, 243, 243); border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(243, 243, 243);">
                <font face="verdana" color="#f28c00"><b>AWS</b></font>&nbsp;<b>Premier Consulting Partner</b>
            </td>
        </tr>
    </tbody>
</table>
</body>
</html>
{% endif %}
