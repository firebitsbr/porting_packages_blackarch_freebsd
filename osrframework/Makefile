PORTNAME=	osrframework
DISTVERSION=	840.e02a6e9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A project focused on providing API and tools to perform more accurate online researches.
WWW=		https://github.com/i3visio/osrframework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cfscrape@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-decorator@${PY_FLAVOR} \
		??/py-emailahoy3@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-oauthlib@${PY_FLAVOR} \
		??/py-pyexcel-io@${PY_FLAVOR} \
		??/py-pyexcel-ods@${PY_FLAVOR} \
		??/py-pyexcel-text@${PY_FLAVOR} \
		??/py-pyexcel-xls@${PY_FLAVOR} \
		??/py-pyexcel-xlsx@${PY_FLAVOR} \
		??/py-pyexcel@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		??/py-validate-email@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
