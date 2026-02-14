PORTNAME=	fimap
DISTVERSION=	230.41eca15
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A little tool for local and remote file inclusion auditing and exploitation.
WWW=		https://gitlab.tha-imax.de/root/fimap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-httplib2@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
