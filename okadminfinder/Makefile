PORTNAME=	okadminfinder
DISTVERSION=	122.a165681
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to find admin panels / admin login pages.
WWW=		https://github.com/mIcHyAmRaNe/okadminfinder3

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-socksio@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-trio@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
