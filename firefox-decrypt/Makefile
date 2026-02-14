PORTNAME=	firefox-decrypt
DISTVERSION=	1.1.2.r1.g4662cb5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract passwords from Mozilla Firefox, Waterfox, Thunderbird, SeaMonkey profiles.
WWW=		https://github.com/unode/firefox_decrypt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/nss \
		??/py-pysqlite3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
