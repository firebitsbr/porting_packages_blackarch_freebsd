PORTNAME=	flare-floss
DISTVERSION=	v3.1.1.r178.g39c2243
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Obfuscated String Solver - Automatically extract obfuscated strings from malware.
WWW=		https://github.com/mandiant/flare-floss

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-halo@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-viv-utils@${PY_FLAVOR} \
		??/vivisect \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
