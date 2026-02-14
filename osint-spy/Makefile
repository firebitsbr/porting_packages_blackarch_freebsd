PORTNAME=	osint-spy
DISTVERSION=	v2.0.r11.g03dcf48
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Performs OSINT scan on email/domain/ip_address/organization.
WWW=		https://github.com/SharadKumar97/OSINT-SPY

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-clearbit@${PY_FLAVOR} \
		??/py-fullcontactpy@${PY_FLAVOR} \
		??/py-prospector@${PY_FLAVOR} \
		??/py-pythonwhois@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-steganography@${PY_FLAVOR} \
		??/sslscan \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
