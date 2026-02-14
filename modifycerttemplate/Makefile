PORTNAME=	modifycerttemplate
DISTVERSION=	7.4c35708
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Aid operators in modifying ADCS certificate templates so that a created vulnerable state can be leveraged for privilege escalation.
WWW=		https://github.com/fortalice/modifyCertTemplate

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-ldap3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
