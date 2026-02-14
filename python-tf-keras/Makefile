PORTNAME=	python-tf-keras
DISTVERSION=	2.20.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	TensorFlow-specific implementation of the Keras API.
WWW=		https://github.com/keras-team/tf-keras

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	??/absl-py \
		??/py-h5py@${PY_FLAVOR} \
		??/py-ml-dtypes@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-optree@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-tensorflow@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/tensorboard \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
