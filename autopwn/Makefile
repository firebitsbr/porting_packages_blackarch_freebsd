PORTNAME=	autopwn
DISTVERSION=	190.fc80cef
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Specify targets and run sets of tools against them.
WWW=		https://github.com/nccgroup/autopwn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/arachni \
		??/cmsmap \
		??/dirb \
		??/enum4linux \
		??/httrack \
		??/hydra \
		??/linenum \
		??/linux-exploit-suggester \
		??/lynis \
		??/metasploit \
		??/nbtscan \
		??/nfs-utils \
		??/nikto \
		??/openssh \
		??/patator \
		??/py-blessings@${PY_FLAVOR} \
		??/py-click-shell@${PY_FLAVOR} \
		??/py-flask-apscheduler@${PY_FLAVOR} \
		??/py-flask-restplus@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-inquirer@${PY_FLAVOR} \
		??/py-pysqlite3@${PY_FLAVOR} \
		??/py-readchar@${PY_FLAVOR} \
		??/py-screenutils@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/skipfish \
		??/sslscan \
		??/sslyze \
		??/testssl.sh \
		lang/python \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
