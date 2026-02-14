PORTNAME=	ldapmonitor
DISTVERSION=	1.4.r13.g6f9dfcb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Monitor creation, deletion and changes to LDAP objects live during your pentest or system administration!
WWW=		https://github.com/p0dalirius/ldapmonitor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ldap3@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sectools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
