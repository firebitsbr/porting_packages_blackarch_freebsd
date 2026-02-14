PORTNAME=	python-bertopic
DISTVERSION=	0.17.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Performs topic Modeling with state-of-the-art transformer models.
WWW=		https://pypi.org/project/bertopic/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-gensim@${PY_FLAVOR} \
		??/py-hdbscan@${PY_FLAVOR} \
		??/py-joblib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-plotly@${PY_FLAVOR} \
		??/py-spacy@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-umap-learn@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
