PORTNAME=	scavenger
DISTVERSION=	103.75907e8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Crawler (Bot) searching for credential leaks on different paste sites.
WWW=		https://github.com/rndinfosecguy/Scavenger

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		??/tmux \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
