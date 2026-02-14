PORTNAME=	ghunt
DISTVERSION=	v2.2.0.r26.g413b577
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An offensive OSINT Google framework.
WWW=		https://github.com/mxrch/GHunt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/# \
		??/https://github.com/mxrch/GHunt/blob/master/pyproject.toml \
		??/py-alive-progress@${PY_FLAVOR} \
		??/py-autoslot@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-beautifultable@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-geopy@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-humanize@${PY_FLAVOR} \
		??/py-imagehash@${PY_FLAVOR} \
		??/py-inflection@${PY_FLAVOR} \
		??/py-jsonpickle@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-protobuf@${PY_FLAVOR} \
		??/py-rich-argparse@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
