PORTNAME=	avet
DISTVERSION=	560.6da43bf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AntiVirus Evasion Tool.
WWW=		https://github.com/govolution/avet

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-charset-normalizer@${PY_FLAVOR} \
		??/py-contourpy@${PY_FLAVOR} \
		??/py-cycler@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-fonttools@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-joblib@${PY_FLAVOR} \
		??/py-kiwisolver@${PY_FLAVOR} \
		??/py-lief@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-mpmath@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-sympy@${PY_FLAVOR} \
		??/py-threadpoolctl@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/wine-mono \
		??/wine_gecko \
		emulators/wine \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
