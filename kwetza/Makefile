PORTNAME=	kwetza
DISTVERSION=	26.0e50272
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python script to inject existing Android applications with a Meterpreter payload.
WWW=		https://github.com/sensepost/kwetza

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/android-apktool \
		??/metasploit \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
