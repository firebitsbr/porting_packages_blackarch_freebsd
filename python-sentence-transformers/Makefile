PORTNAME=	python-sentence-transformers
DISTVERSION=	5.2.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Multilingual text embeddings.
WWW=		https://pypi.org/project/sentence-transformers/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-huggingface-hub@${PY_FLAVOR} \
		??/py-nltk@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pytorch@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-sentencepiece@${PY_FLAVOR} \
		??/py-tokenizers@${PY_FLAVOR} \
		??/py-torchvision@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-transformers@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
