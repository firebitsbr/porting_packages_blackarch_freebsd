PORTNAME=	pureblood
DISTVERSION=	37.2c5ce07
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Penetration Testing Framework created for Hackers / Pentester / Bug Hunter.
WWW=		https://github.com/cr4shcod3/pureblood

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		??/wpscan \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
