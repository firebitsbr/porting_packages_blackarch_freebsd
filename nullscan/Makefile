PORTNAME=	nullscan
DISTVERSION=	1.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular framework designed to chain and automate security tests.
WWW=		http://www.nullsecurity.net/tools/automation.html

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-get-mac@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
