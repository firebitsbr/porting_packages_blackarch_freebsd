PORTNAME=	pepper
DISTVERSION=	18.9dfcade
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source script to perform malware static analysis on Portable Executable.
WWW=		https://github.com/Th3Hurrican3/PEpper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/lief \
		??/py-magic@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		??/yara \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
