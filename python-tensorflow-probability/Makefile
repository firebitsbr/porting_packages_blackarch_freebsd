PORTNAME=	python-tensorflow-probability
DISTVERSION=	0.25.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Probabilistic reasoning and statistical analysis in TensorFlow.
WWW=		https://github.com/tensorflow/probability

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/bazel \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-absl@${PY_FLAVOR} \
		??/py-cloudpickle@${PY_FLAVOR} \
		??/py-decorator@${PY_FLAVOR} \
		??/py-dm-tree@${PY_FLAVOR} \
		??/py-gast@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-tensorflow@${PY_FLAVOR} \
		??/py-tf-keras@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
