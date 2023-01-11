<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
    <head><title></title></head>
    <body style="font-size: 12pt; font-family: Helvetica, sans-serif; color: #222222; overflow-wrap: break-word; -webkit-nbsp-mode: space; line-break: after-white-space;">
        <p>
            <span style="color: #6C1D5F">{{ data['full_name'] }}<br/></span>
            <span>{{ data["job_role"] }}</span>
            {% if 'unit' in data and data['unit'] %}
                <span>/</span>
                <span style="color: #A1A1A1;">{{data['unit']}}</span>
            {% endif %}
        </p>
        <p>
            <img width="155" height="55" id="Xebia" src="https://assets.oblcc.com/xebia/xebia.png" alt="Xebia" name="Xebia" />
        </p>
        <p>
            M <a style="text-decoration: none; color: #222222;" href="tel:{{data['phone'].replace(' ', '')}}">{{ data["phone"] }}</a><br/>
            <a style="text-decoration: none; color: #222222;" href="mailto:{{ data["email"] }}">
                <span>{{ data["email"] }}</span>
            </a>
        </p>
        <p>
            <span>Laapersveld 27</span><br/>
            <span>1213 VB Hilversum</span><br/>
            <span>The Netherlands</span><br/>
            <span>T <a style="text-decoration: none; color: #222222;" href="tel:+31355381921">+31 35 53 81 921</a></span>
        </p>
        <p>
            <a href="https://www.facebook.com/xebianl/" title="Facebook" ><img border="0" width="19" height="19" id="Facebook" src="https://assets.oblcc.com/xebia/facebook.png" alt="Facebook" name="Facebook" /></a>
            <a href="https://twitter.com/xebia" title="Twitter"><img border="0" width="19" height="19" id="Twitter" src="https://assets.oblcc.com/xebia/twitter.png" alt="Twitter" name="Twitter" /></a>
            {% if 'linkedin_url' in data and data['linkedin_url'] %}
            <a href="{{ data['linkedin_url'] }}" ><img border="0" width="19" height="19" id="LinkedIn" src="https://assets.oblcc.com/xebia/linkedin.png" alt="LinkedIn" name="LinkedIn" /></a>
            {% endif %}
            <a href="https://www.instagram.com/xebianl/" title="https://www.instagram.com/xebianl/" ><img border="0" width="20" height="19" id="Instagram" src="https://assets.oblcc.com/xebia/instagram.png" alt="Instagram" name="Instagram" /></a>
            <a href="https://www.youtube.com/user/XebiaNL" title="YouTube"><img border="0" width="19" height="19" id="YouTube" src="https://assets.oblcc.com/xebia/youtube.png" alt="YouTube" name="YouTube" /></a>
            {% if 'github_url' in data and data['github_url'] %}
            <a href="{{ data['github_url'] }}" ><img border="0" width="19" height="19" id="Github" src="https://assets.oblcc.com/xebia/github.png" alt="Github" name="Github" /></a>
            {% endif %}
        </p>
    </body>
</html>
