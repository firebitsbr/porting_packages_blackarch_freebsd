PORTNAME=	tweets-analyzer
DISTVERSION=	55.8d6bd3c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tweets metadata scraper & activity analyzer.
WWW=		https://github.com/x0rz/tweets_analyzer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-ascii_graph@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
