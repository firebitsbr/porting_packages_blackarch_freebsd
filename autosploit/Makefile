PORTNAME=	autosploit
DISTVERSION=	v4.0.r2.g9a6a5ef
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automate the exploitation of remote hosts.
WWW=		https://github.com/NullArray/AutoSploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/metasploit \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-blessings@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/sudo \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
