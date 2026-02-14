PORTNAME=	pulsar
DISTVERSION=	55.3c61178
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Protocol Learning and Stateful Fuzzing.
WWW=		https://github.com/hgascon/pulsar

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cuckoo \
		??/py-levenshtein@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-pygraphviz@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
