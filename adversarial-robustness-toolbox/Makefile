PORTNAME=	adversarial-robustness-toolbox
DISTVERSION=	1.20.1.r155.g23539e2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python Library for Machine Learning Security.
WWW=		https://github.com/Trusted-AI/adversarial-robustness-toolbox

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-numpy@${PY_FLAVOR} \
		??/py-pytorch@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
