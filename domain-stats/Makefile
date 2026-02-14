PORTNAME=	domain-stats
DISTVERSION=	169.759c52c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A web API to deliver domain information from whois and alexa.
WWW=		https://github.com/MarkBaggett/domain_stats

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-munge@${PY_FLAVOR} \
		??/py-publicsuffixlist@${PY_FLAVOR} \
		??/py-rdap@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
