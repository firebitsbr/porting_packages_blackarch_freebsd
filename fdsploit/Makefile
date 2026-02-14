PORTNAME=	fdsploit
DISTVERSION=	26.4522f53
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A File Inclusion & Directory Traversal fuzzing, enumeration & exploitation tool.
WWW=		https://github.com/chrispetrou/FDsploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-validators@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
