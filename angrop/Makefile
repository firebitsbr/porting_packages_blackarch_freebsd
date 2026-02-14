PORTNAME=	angrop
DISTVERSION=	v9.2.12.post3.r65.gf8bb3ef
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A rop gadget finder and chain builder.
WWW=		https://github.com/angr/angrop

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/angr \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
