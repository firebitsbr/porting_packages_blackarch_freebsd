PORTNAME=	cleverhans
DISTVERSION=	v4.0.0.r7.g574efc1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library to benchmark machine learning systems vulnerability to adversarial examples.
WWW=		https://github.com/cleverhans-lab/cleverhans

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-absl@${PY_FLAVOR} \
		??/py-easydict@${PY_FLAVOR} \
		??/py-joblib@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-mnist@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pycodestyle@${PY_FLAVOR} \
		??/py-pytorch@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-tensorflow-probability@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
