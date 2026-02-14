PORTNAME=	python-top2vec
DISTVERSION=	1.0.36
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Learns jointly embedded topic, document and word vectors.
WWW=		https://pypi.org/project/top2vec/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-gensim@${PY_FLAVOR} \
		??/py-hdbscan@${PY_FLAVOR} \
		??/py-joblib@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-umap-learn@${PY_FLAVOR} \
		??/py-wordcloud@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
