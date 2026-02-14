PORTNAME=	weevely
DISTVERSION=	928.3d62e88
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Weaponized web shell.
WWW=		http://epinna.github.io/Weevely/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
